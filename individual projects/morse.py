# DP morse code
# translator for morse code

# Created tuples for English and corresponding Morse cods
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
    "--...", "---..", "----.", " "
)

# Function to translate English to M Code
def english_to_morse(text):
    morset = []
    text = text.upper()  # turns all into uppercase
    for char in text:
        if char in english_letters:
            index = english_letters.index(char)
            morset.append(morsesymbols[index])
        else:
            # for non existing characters in tuple
            morset.append("?")
    # Join morse Code with spaces between letters
    return " ".join(morset)

# Function to translate morse Code to english 
def morse_to_english(code):
    engt = []
    # Split Morse Code into symbols using a space as separattor
    morse_symbols = code.split(" ")
    for symbol in morse_symbols:
        if symbol in morsesymbols:
            index = morsesymbols.index(symbol)
            engt.append(english_letters[index])
        else:
            # Handle invalid Morse Code symnbols
            engt.append("?")
    # Join english together making string
    return "".join(engt)

# MAIN LOOP
def main():
    print("This is the Morse Code translator")
    print("yOu can translate English to morse Code or oppossite")
    
    while True:
        # Display main menu
        print("MAIN MENU:")
        print("1 Translated from Morse Code to English")
        print("2 Translate from English to Morse Code")
        print("3. EXIt")
        choice = input("Please enter your choice 1 2. or 3): ")
        
        if choice == "1":
            morse_input = input("enter Morse Code (use spaces between letters too seperat): ")
            result = morse_to_english(morse_input)
            print("translated  to Englsish:", result)
        
        elif choice == "2":
            eng_inp = input("Enter English text to translate to Morse Code: ")
            result = english_to_morse(eng_inp)
            print("Translated to Morse Code res ult:", result)
        
        elif choice == "3":
            print("Thanks for using translator")
            break
        
        else:
            # Detect invalid input
            print("Invalid choice. Please select 1 2, or 3")

# Call s main functions
main()
