# Document Word Count Updater basically Main Menu
from File import read_file, write_file, append_content
from view import display_document
from time_1 import get_formatted_time
 #functions contained seperate files

def get_file_path():
    #ask for fil path
    file_path = input("enter the exact file path for your document: ").strip()
    return file_path




def update_document_info(file_path):
    #update word count and time
    try:
        content = read_file(file_path)
        word_count = len(content.split())
        current_time = get_formatted_time()
        
        write_file(file_path, content, word_count, current_time)
        print(f"Document updated. Word count: {word_count}")
        
    except FileNotFoundError:
        print("Error is File not found amake sure file path is real")
    except Exception as e:
        print(f"Error updating the document: {e}")


def view_document(file_path):
    #2ith function display document
    try:
        content = read_file(file_path)
        display_document(content)

 
    except FileNotFoundError:
        print("Error is File not found amake sure file path is real")
    except Exception as e:
        print(f"error whenreading document: {e}")


def add_content_to_document(file_path):
    #new content
    try:
        print("enter new content enter 2 times to end :")
        lines = []
        
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        
        new_content = "\n".join(lines)
        
        if new_content.strip():
            append_content(file_path, new_content)
            print("Content added successfully. good")
        else:
            print("pluh ")
            
    except FileNotFoundError:
        print("file path not found")
    except Exception as e:
        print(f"Error inadding content: {e}")


def display_menu():
    #displays the main menu
    print("\n Document Word Count Updater ")
    print("1 Update document info")
    print("2 View document")
    print("3 Add content to document")
    print("4d Exit")


def main():
    #main loop with functions
    file_path = ""
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            file_path = get_file_path()
            update_document_info(file_path)
            
        elif choice == "2":
            if file_path:
                view_document(file_path)
            else:
                print("need file path START WITH OPTIO 1")
                
        elif choice == "3":
            if file_path:
                add_content_to_document(file_path)
            else:
                print("need file path START WITH OPTIO 1")
                
        elif choice == "4":
            print("beebye")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


main()
