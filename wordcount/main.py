# Document Word Count Updater - Main Menu
from file_handler import read_file, write_file, append_content
from view import display_document
from time_handler import get_formatted_time


def get_file_path():
    """Get the file path from the user."""
    file_path = input("Enter the exact file path for your document: ").strip()
    return file_path


def update_document_info(file_path):
    """Update word count and timestamp in the document."""
    try:
        content = read_file(file_path)
        word_count = len(content.split())
        current_time = get_formatted_time()
        
        write_file(file_path, content, word_count, current_time)
        print(f"Document updated. Word count: {word_count}")
        
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"Error updating document: {e}")


def view_document(file_path):
    """Display the document content."""
    try:
        content = read_file(file_path)
        display_document(content)
        
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"Error reading document: {e}")


def add_content_to_document(file_path):
    """Add new content to the document."""
    try:
        print("Enter new content (press Enter twice to finish):")
        lines = []
        
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        
        new_content = "\n".join(lines)
        
        if new_content.strip():
            append_content(file_path, new_content)
            print("Content added successfully.")
        else:
            print("No content added.")
            
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"Error adding content: {e}")


def display_menu():
    """Display the main menu."""
    print("\n--- Document Word Count Updater ---")
    print("1. Update document info")
    print("2. View document")
    print("3. Add content to document")
    print("4. Exit")


def main():
    """Main program loop."""
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
                print("Please set a file path first (option 1).")
                
        elif choice == "3":
            if file_path:
                add_content_to_document(file_path)
            else:
                print("Please set a file path first (option 1).")
                
        elif choice == "4":
            print("Exiting. Thank you for using Document Word Count Updater!")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()