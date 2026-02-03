# DP morse code
#translator for mors evcoeeode

# Create tuples for english and corrsponfing morse
english_letters = (
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "
)

morsesymbols = (
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
    "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
    "-----", ".----", "..---", "...--", "....-", ".....", "-....", 
    "--...", "---..", "----.", "/"
)

# Function to translate English  to Morse Code
def english_to_morse(text):
    morset = []
    text = text.upper()  # turns all into uppercas
    for char in text:
        if char in english_letters:
            index = english_letters.index(char)
            morset.append(morsesymbols[index])
        else:
            # for non existing chrachters in tuple
            morset.append("?")
    # Join Morse Code with spaces between letters
    return " ".join(morset)

# Funct to translate morse Code to English 
def morse_to_english(code):
    engt = []
    # Split Morse Code into symbols using a space as separator
    morse_symbols = code.split(" ")
    for symbol in morse_symbols:
        if symbol in morsesymbols:
            index = morsesymbols.index(symbol)
            engt.append(english_letters[index])
        else:
            # Handle invalid Morse Code symbols
            engt.append("?")
    # Join English together makinn string
    return "".join(engt)



# MAIN LOOP
def main():
    print("this is the morse code translator")
    print("You can translate English to Morse Code or opposite")
    
    while True:
        # Display main menu
        print("MAIN MENU:")
        print("1. Translate from theCode to English")
        print("2. Translate from english to Morse Code")
        print("3. exit")
        choice = input("Please enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            morse_input = input("enter Morse Code use / to signal  space: ")
            result = morse_to_english(morse_input)
            print("trranslated to English:", result)
        
        elif choice == "2":
            english_input = input("Enter english text to translate to Morse Code: ")
            result = english_to_morse(english_input)
            print("translated to Morse Code:", result)
        

        elif choice == "3":
            print("Thank you for using the morse Code Translateor")
            break
        
        else:
            # detect invalidd input
            print("Invalid choice. PLease select 1, 2, or 3.")

# call mian function
if __name__ == "__main__":
    main()
