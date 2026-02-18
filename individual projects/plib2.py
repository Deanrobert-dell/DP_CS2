
import csv
#
def load():
    try:
        with open("library.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(row)
    except:
        pass

def save():
    with open("library.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "author", "year", "genre"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)  #turns into dictionary
        writer.writeheader()
        writer.writerows(books)
    print("Library saved")


def main(): 
        #intoduce them to lib manager
        print("Welcome to a library mannager")
        load() #saves it between runs puts it in books list
        while True:
          print("\nType the number for the action you would like to perform:")
          print("1. View simple list")
          print("2. Add item")
          print("3. Upsdate item")
          print("4. Remove item")
          print("5. Search")
          print("6 save library")
          print("7. Exit")
      
          choice = input("Enter achoice: ")
      
          if choice == "1":
              view()
          elif choice == "2":
              add()
          elif choice == "3":
              update()
          elif choice == "4":
              remove()
          elif choice == "5":
              search()
          elif choice == "6":
              save()
          elif choice == "7":
              save()
              break
          else:
              print("Invalid choice. Try again. (stupid)")
 #function that appends names and authors
def add():
    book = input("What is the title of the book youre adding??: ")
    aut = input("what is the author of it: ")
    year = input("What is the year: ")
    genre = input("What is the genrse: ")
    newbook = {"title": book, "author": aut, "year": year, "genre": genre}
    books.append(newbook)
    print("You have added:", book)
#is for statement to see if a aneme is in the list (def search)
def search():
    term = input("eNter a book title or author to search: ")
    found = False
    for book in books:
        if term.lower() in book["title"].lower() or term.lower() in book["author"].lower():
            print(book["title"], "by", book["author"])
            found = True
    if found == False:
        print("Book isnot found")

#just do opposite of eppend, use .remove
def remove(): 
    book = input("What is the title of the book yourre trying to removing: ")
    aut = input("what is the author: ")
    found = False
    for item in books:
        if item["title"] == book and item["author"] == aut:
            books.remove(item)
            print("You have removed:", book)
            found = True
            break
    if found == False:
        print("That book is not in the library")

def update():
    book = input("What is the title of the book you'are updating: ")
    aut = input("What is the author: ")
    for item in books:
        if item["title"] == book and item["author"] == aut:
            item["title"] = input("New title: ")
            item["author"] = input("New author: ")
            item["year"] = input("New year: ")
            item["genre"] = input("New genre: ")
            print("Book updated")
            return
    print("Book not found")


def view():
    mode = input("Simpleified view(1) or detailed view of all of it(2): ")
    if mode == "1":
        for book in books:
            print(book["title"], "by", book["author"])
    elif mode == "2":
        for book in books:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            print("Genre:", book["genre"])
            print("pluh")
        
#long list of books
books = []
#call main functioj
main()
