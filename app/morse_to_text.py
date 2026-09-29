from .morse_data import reverse_code

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
