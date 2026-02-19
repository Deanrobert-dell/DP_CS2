#DP cs2 word counter
from File import update_document  # ensure myapp/storage.py defines it
update_document(42, {"title": "New title"})

from view import print_docs

from append import add_to_document

import File #
# MAIN LOOP
def main():
    print("this is a word counter with time recording")
    print("you can update docs, view docs, add to docs, and exit")
    
    while True:
        # Display main menu
        print("MAIN MENU:")
        print("1 Update Docs")
        print("2. View Docs")
        print("3. Add to Docs")
        print("4. Exit")
        choice = input("PPlease enter your choice (1-4): ")

        if choice == "1":
            doc_name = input("Enter the document name to update: ")
            new_content = input("Enter the new content: ")
            update_document(doc_name, new_content) #

        elif choice == "2":
            print_docs()

        elif choice == "3":
            doc_name = input("Enter the document name to add to: ")
            additional_content = input("Enter the additional content: ")
            add_to_document(doc_name, additional_content)

        elif choice == "4":
            print("Thanks for using the word counter")
            break

        else:
            # Detect invalid input
            print("Invalid choice. Please select 1 2, or 3")
#main called function
# Call s main functions

main()




