import string

def alphabet_position(letter):
    alphabet = string.ascii_lowercase
    alphabetupper = string.ascii_uppercase
    if letter in alphabetupper:
        letter = letter.lower()
    return alphabet.index(letter)


def rotate_character(char, rot):
    alphabet = string.ascii_lowercase
    alphabetupper = string.ascii_uppercase
    if not char.isalpha():
        return char
    else:
        newposition = (alphabet_position(char) + int(rot))%26

        if char.isupper():
            return alphabetupper[newposition]#char = char.upper()
        else:
            return alphabet[newposition]

def encrypt(text, rot):
        encrypted = ""
        for char in text:
            encrypted = encrypted + rotate_character(char,rot)
        return encrypted
