

#
def main(): 
    #intoduce them to lib manager
    print("Welcome to a library mannager")
    choice = input("Do you want to view(1), add(2), remove(3), search(4) or exit(5): ")
#choice with numbers calling each funciton and a final quit one
    while choice != "5":
        if choice == "1":
            print(books)
        elif choice == "2":
            add()
        elif choice == "3":
            remove()
        elif choice == "4":
            search()
        else:
            print("Invalid choice")
#ask again for repeatabilit, so its in the loop
        choice = input("Do you want to viiew(1), add(2), remove(3), search(4) or exit(5): ")
 #function that appends names and authors
def add():
    book = input("What is the title of the book youre adding: ")
    aut = input("What is the author: ")
    full = book + " by " + aut
    books.append(full)
    print("You have added:", full)
#is for statement to see if a aneme is in the list (def search)
def search():
    term = input("eNter a book title or author to search: ")
    found = False
    for book in books:
        if term in book:
            print(book)
            found = True
    if found == False:
        print("Book isnot found")

#just do opposite of eppend, use .remove
def remove(): 
    book = input("What is the title of the book you're removing: ")
    aut = input("What is the author: ")
    full = book + " by " + aut
    if full in books:
        books.remove(full)
        print("You have removed:", full)
    else:
        print("That book is not in the library")
        
#long list of books
books = [
    "The Hobbit by J.R.R Tolkien",
    "A Wrinkle in Time by Madeleine LEngle",
    "Steelheart by Brandon Sanderson",
    "The Chronicles of Narnia: The Horse and His Boy by C.S. Lewis",
    "The Giver by Lois Lowry",
    "Howls Moving Castle by Diana Wynne Jones",
    "Artemis Fowl by Eoin Colfer",
    "Fablehaven by Brandon Mull",
    "Inkheart by Cornelia Funke"
]
#call main functioj
main()
