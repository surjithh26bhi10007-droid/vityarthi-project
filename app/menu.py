from app.text_to_morse import text_to_morse
from app.morse_to_text import morse_to_text

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
