from .morse_data import morse_code

def text_to_morse(text):
    result = ""

    for letter in text.upper():

        if letter in morse_code:
            result = result + morse_code[letter] + " "

        elif letter == " ":
            result = result + "  "

    return result
