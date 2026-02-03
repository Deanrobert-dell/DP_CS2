# MORSE CODE TRANSLATOR PROGRAM
# This program allows the user to translate between English and Morse Code

# Create tuples for English letters and their corresponding Morse Code symbols
english_letters = (
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "
)

morse_code_symbols = (
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
    "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
    "-----", ".----", "..---", "...--", "....-", ".....", "-....", 
    "--...", "---..", "----.", "/"
)

# Function to translate English text to Morse Code
def english_to_morse(text):
    morse_translation = []
    text = text.upper()  # Convert input to uppercase for matching
    for char in text:
        if char in english_letters:
            index = english_letters.index(char)
            morse_translation.append(morse_code_symbols[index])
        else:
            # Handle characters that are not in the English letters tuple
            morse_translation.append("?")
    # Join Morse Code with spaces between letters
    return " ".join(morse_translation)

# Function to translate Morse Code to English text
def morse_to_english(code):
    english_translation = []
    # Split Morse Code input into symbols using space as separator
    morse_symbols = code.split(" ")
    for symbol in morse_symbols:
        if symbol in morse_code_symbols:
            index = morse_code_symbols.index(symbol)
            english_translation.append(english_letters[index])
        else:
            # Handle invalid Morse Code symbols
            english_translation.append("?")
    # Join English letters to form a string
    return "".join(english_translation)

# MAIN LOOP
def main():
    print("Welcome to the Morse Code Translator!")
    print("You can translate English to Morse Code or Morse Code to English.")
    
    while True:
        # Display main menu
        print("\nMAIN MENU:")
        print("1. Translate from Morse Code to English")
        print("2. Translate from English to Morse Code")
        print("3. Exit")
        
        choice = input("Please enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            morse_input = input("Enter Morse Code (use '/' for space between words): ")
            result = morse_to_english(morse_input)
            print("Translated to English:", result)
        
        elif choice == "2":
            english_input = input("Enter English text to translate to Morse Code: ")
            result = english_to_morse(english_input)
            print("Translated to Morse Code:", result)
        
        elif choice == "3":
            print("Thank you for using the Morse Code Translator. Goodbye!")
            break
        
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
