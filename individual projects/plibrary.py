#
def add():


def search():


def remove():


def main(): 
    print(" welcome to a library manager")
    choice = input(" do you want to view(1), add(2), remove(3), search(4) or exit(5), the library")
    
    while choice != "5":
        if choice == "1":
            
        elif choice == "2":
            add()
        elif choice == "3":
            remove()
        elif choice == "4":
            search()
        choice = input(" do you want to view(1), add(2), remove(3), search(4) or exit(5), the library")

books = ["The Hobbit by J.R.R Tolkien", "A Wrinkle in Time by Madeleine LEngle", "Steelheart by Brandon Sanderson:", "The Chronicles of Narnia: The Horse and His Boy by C.S. Lewis", "The Giver by Lois Lowry", "Howls Moving Castle by Diana Wynne Jones", "Artemis Fowl by Eoin Colfer", "Fablehaven by Brandon Mull", "Inkheart by Cornelia Funke",]
