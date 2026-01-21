#
def main(): 
    print(" welcome to a library manager")
    choice = input(" do you want to view(1), add(2), remove(3), search(4) or exit(5), the library")
    
    while choice != "5":
        if choice == "1":
            print(books)
        elif choice == "2":
            add()
        elif choice == "3":
            remove()
        elif choice == "4":
            search()
        choice = input(" do you want to view(1), add(2), remove(3), search(4) or exit(5), the library")

def add():
    book = input("what is the title of the book your adding: ")
    aut = input("what is the authot")
    full = (book+ aut)
    print("you have added: ", book, "by ", aut)
    books.append(full)

def search():



def remove(): 
    book = input("what is the title of the book your removing: ")
    aut = input("what is the authot")
    full = (book+ aut)
    print("you have removed: ", book, "by ", aut)
    books.remove(full)




books = ["The Hobbit by J.R.R Tolkien", "A Wrinkle in Time by Madeleine LEngle", "Steelheart by Brandon Sanderson:", "The Chronicles of Narnia: The Horse and His Boy by C.S. Lewis", "The Giver by Lois Lowry", "Howls Moving Castle by Diana Wynne Jones", "Artemis Fowl by Eoin Colfer", "Fablehaven by Brandon Mull", "Inkheart by Cornelia Funke",]
