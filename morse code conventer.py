
morse_code = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.'}

reverse_code = {}

for letter in morse_code:
    reverse_code[morse_code[letter]] = letter

def text_to_morse(text):
    result = ""

    for letter in text.upper():

     if letter in morse_code:
      result = result + morse_code[letter] + " "

     elif letter == " ":
      result = result + "  "

    return result

def morse_to_text(code):
    result = ""

    words = code.split("  ")

    for word in words:

     letters = word.split()
        
    for letter in letters:

     if letter in reverse_code:
      result = result + reverse_code[letter]

     result = result + " "

    return result

while True:

    print("\n==============================|")
    print("      MORSE CODE CONVERTER    |")
    print("==============================|")
    print("1. Text to Morse Code         |")
    print("2. Morse Code to Text         |")
    print("3. Exit                       |")
    print("==============================|")

    choice = input("Enter your choice: ")
    if choice == "1":

        text = input("Enter text: ")

        result = text_to_morse(text)

        print("Morse Code:", result)

    elif choice == "2":

        code = input("Enter Morse Code: ")

        result = morse_to_text(code)

        print("Text:", result)

    elif choice == "3":

        print("Thank you for using Morse Code Converter!")
        break

    else:

        print("Invalid choice!")
        print("Please enter 1, 2, or 3.")

