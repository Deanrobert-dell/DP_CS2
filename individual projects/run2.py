import csv 

file_path = "individual projects\\movies.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        
        # If you want to save all rows, create a master list
        all_movies = []

        for line in content:
            # Create a dictionary using the indices you were printing
            movie_dict = {
                "id": line[1],
                "title": line[2],
                "year": line[3],
                "genre": line[4],
                "rating": line[5]
            }
            
            all_movies.append(movie_dict)
            print(movie_dict) # This replaces your 5 print statements

except FileNotFoundError:
    print("file not found")

#rix