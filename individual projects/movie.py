import csv

file = "individual projects/movies.csv"


# turns the file into a list
def load_movies():
    movies = []

    try:
        with open(file, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                try:
                    # Store each movie as a dictionary
                    movie = {
                        "title": row["Title"].strip(),
                        "director": row["Director"].strip().lower(),
                        "genres": [g.strip().lower() for g in row["Genre"].split("/")], #use g for grnre
                        "actors": [a.strip().lower() for a in row["Notable Actors"].split(",")], #use a for actors
                        "length": int(row["Length (min)"])
                    }
                    movies.append(movie)
                except:
                    # skips rows with errors
                    continue

    except FileNotFoundError:
        print("Errors movie file not found")
    except PermissionError:
        print("Errorno permission to read the file ")

    return movies


# filters movie using th genre
def filter_genre(movies, genre):
    genre = genre.lower()
    return [m for m in movies if any(genre in g for g in m["genres"])] #repeatedly use this as a system to check if genere is in the lsi of genres, using the for loops 


# Filters movies by director
def filter_director(movies, director):
    director = director.lower() #put in lowercase for better ereadability
    return [m for m in movies if director in m["director"]] #check of directos are


# Filters movies by actors
def filter_actor(movies, actor):
    actor = actor.lower()
    return [m for m in movies if any(actor in a for a in m["actors"])]#check if actor is in the list of actors for each movi

# Filters movies by lenth range inncolumn
def filter_length(movies, min_len, max_len):
    results = []

    for m in movies:
        length = m["length"] #snatches data from file

        if length < min_len:   
            continue
        if length > max_len:   #find length from user
            continue

        results.append(m)

    return results


# use all the functions to deternine final movies
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


# Prints movies in good way
def print_movies(movies):
    for m in movies:
        print(
            f'Title: "{m["title"]}"  ' #here and below have space to seperate ethe feild better, prints it by colums
            f'Genres: {(m["genres"]).title()}  '
            f'Director: {m["director"].title()}  '
            f'Length: {m["length"]} min'
        )


# Prints the full movie list
def print_full_list(movies):
    print("\nFULL M0VIE LiST:\n")
    print_movies(movies)


# main menu to search
def search_movies(movies):
    print("\nchoose filters to apply (comma separated)d:")
    print("1. Genre")
    print("2. director")
    print("3. Actor")
    print("(4) Length (min/+max)")

    choice = input("Example:s 1,3 or 2,4 → ").split(",")

    filters = {} #empty dicst to store the filters that the user wants to apply later ON the road

    if "1" in choice:
        filters["genre"] = input("Enter genres: ")

    if "2" in choice:
        filters["director"] = input("Enter dsirector name: ")

    if "3" in choice:
        filters["actor"] = input("enter actor name: ")

    if "4" in choice:
        min_input = input("Enter minimum length (): ")
        max_input = input("Enter maximum length (: ")

        min_len = int(min_input) #uses the defined data from user (some thing below)
        max_len = int(max_input)

        filters["length"] = (min_len, max_len)

    results = apply_filters(movies, filters)

    print("\nRESULTS:\n")

    if results == []: #see iaf its is blank
        print("no movies match those filters.")
        print("Try removing one filter or morewidening the length range.")
    else:
        print_movies(results)


# Main program loops forever)
def main():
    movies = load_movies()

    print("welcome to the Movie Recommendertion sytem!")
    print("Search movies using genre, director, actor, or length. to find what yoy want")

    while True:
        print("\nMAIN MENU")#ask what they want to do
        print("1 Search ")
        print("2. se list")
        print("3 Exit")

        choice = input("Epleas ter your choice: ")

        if choice == "1":# now just see wht they chsoe and call a function
            search_movies(movies)
        elif choice == "2":
            print_full_list(movies)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Your stupid (respectfully) do 1 2 or 3")


main()