import csv

file = "individual projects/movies.csv"


# turns the file into a list
def load_movies():
    movies = []

    try:
        with open(file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    # Store each movie as a dictionary
                    movie = {
                        "title": row["Title"].strip(),
                        "director": row["Director"].strip().lower(),
                        "genres": [g.strip().lower() for g in row["Genre"].split("/")],
                        "actors": [a.strip().lower() for a in row["Notable Actors"].split(",")],
                        "length": int(row["Length (min)"])
                    }
                    movies.append(movie)
                except:
                    # skips rows with errors
                    continue

    except FileNotFoundError:
        print("Error: movie file not found.")
    except PermissionError:
        print("Error: no permission to read the file.")

    return movies


# Filters movies by genre
def filter_genre(movies, genre):
    genre = genre.lower()
    return [m for m in movies if any(genre in g for g in m["genres"])]


# Filters movies by director
def filter_director(movies, director):
    director = director.lower()
    return [m for m in movies if director in m["director"]]


# Filters movies by actor
def filter_actor(movies, actor):
    actor = actor.lower()
    return [m for m in movies if any(actor in a for a in m["actors"])]


# Filters movies by length range
def filter_length(movies, min_len, max_len):
    results = []

    for m in movies:
        length = m["length"]

        if min_len is not None and length < min_len:
            continue
        if max_len is not None and length > max_len:
            continue

        results.append(m)

    return results


# Applies all selected filters using AND logic
def apply_filters(movies, filters):
    results = movies

    if "genre" in filters:
        results = filter_genre(results, filters["genre"])

    if "director" in filters:
        results = filter_director(results, filters["director"])

    if "actor" in filters:
        results = filter_actor(results, filters["actor"])

    if "length" in filters:
        min_len, max_len = filters["length"]
        results = filter_length(results, min_len, max_len)

    return results


# Prints movies in a readable format
def print_movies(movies):
    for m in movies:
        print(
            f'Title: "{m["title"]}" — '
            f'Genres: {"|".join(m["genres"]).title()} — '
            f'Director: {m["director"].title()} — '
            f'Length: {m["length"]} min'
        )


# Prints the full movie list
def print_full_list(movies):
    print("\nFULL MOVIE LIST:\n")
    print_movies(movies)


# Handles the search flow
def search_movies(movies):
    print("\nChoose filters to apply (comma separated):")
    print("1. Genre")
    print("2. Director")
    print("3. Actor")
    print("4. Length (min/max)")

    choice = input("Example: 1,3 or 2,4 → ").split(",")

    filters = {}

    if "1" in choice:
        filters["genre"] = input("Enter genre: ")

    if "2" in choice:
        filters["director"] = input("Enter director name: ")

    if "3" in choice:
        filters["actor"] = input("Enter actor name: ")

    if "4" in choice:
        min_input = input("Enter minimum length (or leave blank): ")
        max_input = input("Enter maximum length (or leave blank): ")

        min_len = int(min_input) if min_input else None
        max_len = int(max_input) if max_input else None

        filters["length"] = (min_len, max_len)

    results = apply_filters(movies, filters)

    print("\nRESULTS:\n")

    if not results:
        print("No movies match those filters.")
        print("Try removing one filter or widening the length range.")
    else:
        print_movies(results)


# Main program loop
def main():
    movies = load_movies()

    print("Welcome to the Movie Recommender!")
    print("Search movies using genre, director, actor, or length.")

    while True:
        print("\nMAIN MENU")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_movies(movies)
        elif choice == "2":
            print_full_list(movies)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()