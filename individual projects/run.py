import csv 

file_path = "individual projects\\movies.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[1])
            print(line[2])
            print(line[3])
            print(line[4])
            print(line[5])
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("no permission")






