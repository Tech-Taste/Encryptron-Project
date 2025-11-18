# -*- coding: utf-8 -*-

"""
File: Final_Project.py

Brief description:
The program allows the user to choose from two predefined encryption
systems (Morse code and Hexadecimal), or to use the user's own
system through the customizer to encrypt or decrypt (only Morse code
and Hexadecimal) a message.

Students' Name:
    # José Fernando Rodríguez Amaro
    # Karla Regina Carmona Martínez
    # Brayton William Rodriguez Gallegos
    # Diego Alejandro Cantú Pozo

Course Name: Introduction to Programming

Date Created: 11-10-2025
Date Last Modified: 11-15-2025
"""

"""
morse_dict stores all the predefined key:value groups for Morse code encryption and decryption.
For Morse code, every letter is uppercase.
Alphanumerical characters are the key and their equivalents are the values in this dictionary.
"""

morse_dict = {
    "A":"._",
    "B":"_...",
    "C":"_._.",
    "D":"_..",
    "E":".",
    "F":".._.",
    "G":"__.",
    "H":"....",
    "I":"..",
    "J":".___",
    "K":"_._",
    "L":"._..",
    "M":"__",
    "N":"_.",
    "O":"___",
    "P":".__.",
    "Q":"__._",
    "R":"._.",
    "S":"...",
    "T":"_",
    "U":".._",
    "V":"..._",
    "W":".__",
    "X":"_.._",
    "Y":"_.__",
    "Z":"__..",
    "0":"_____",
    "1":".____",
    "2":"..___",
    "3":"...__",
    "4":"...._",
    "5":".....",
    "6":"_....",
    "7":"__...",
    "8":"___..",
    "9":"____."
}

"""
hex_dict works almost the same as morse_dict, but this dictionary stores other key:value groups,
like the blank space " ", coma ",", and the lower case letters definitions.
"""

hex_dict = {
    " ":"20",
    "0":"30",
    "1":"31",
    "2":"32",
    "3":"33",
    "4":"34",
    "5":"35",
    "6":"36",
    "7":"37",
    "8":"38",
    "9":"39",
    "A":"41",
    "B":"42",
    "C":"43",
    "D":"44",
    "E":"45",
    "F":"46",
    "G":"47",
    "H":"48",
    "I":"49",
    "J":"4A",
    "K":"4B",
    "L":"4C",
    "M":"4D",
    "N":"4E",
    "O":"4F",
    "P":"50",
    "Q":"51",
    "R":"52",
    "S":"53",
    "T":"54",
    "U":"55",
    "V":"56",
    "W":"57",
    "X":"58",
    "Y":"59",
    "Z":"5A",
    "a":"61",
    "b":"62",
    "c":"63",
    "d":"64",
    "e":"65",
    "f":"66",
    "g":"67",
    "h":"68",
    "i":"69",
    "j":"6A",
    "k":"6B",
    "l":"6C",
    "m":"6D",
    "n":"6E",
    "o":"6F",
    "p":"70",
    "q":"71",
    "r":"72",
    "s":"73",
    "t":"74",
    "u":"75",
    "v":"76",
    "w":"77",
    "x":"78",
    "y":"79",
    "z":"7A",
    ",":"2C"
}

"""
new_dict is an empty dictionary that will store the user's custom definitions.
"""

new_dict = {}

"""
The menu function works as a main hub for all the subroutines.
The while True loop allows the user to do multiple operations without restarting the program over and over again.

After displaying the multiple options, the function asks the user for a numerical input.
try-except ValueError helps to prevent the code interruption due to an invalid input.
This way, the user can only use numerical values.
After that, depending on the input, the corresponding function is called.
"""

def menu():
    while True:
        print("Welcome to the Encryptron!")
        print("\n1. Morse Code to Text")
        print("2. Text to Morse Code")
        print("3. Hexadecimal to Text")
        print("4. Text to Hexadecimal")
        print("5. Add a New Encryption System")
        print("6. Encryption with Personalized System")
        print("7. Exit")

        try:
            menu_choice = int(input("\nPlease enter your choice (number): "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if menu_choice == 1:
            print("You have chosen: Morse Code to Text")
            morse_to_text()
        elif menu_choice == 2:
            print("You have chosen: Text to Morse Code")
            text_to_morse()
        elif menu_choice == 3:
            print("You have chosen: Hexadecimal to Text")
            hexadecimal_to_text()
        elif menu_choice == 4:
            print("You have chosen: Text to Hexadecimal")
            text_to_hexadecimal()
        elif menu_choice == 5:
            print("You have chosen: Add a New Encryption System")
            create_customized_dict()
        elif menu_choice == 6:
            print("You have chosen: Encryption with Personalized System")
            customized_encryption()
        elif menu_choice == 7:
            print("\nThanks for using the Encryptron!")
            quit()
        else:
            print("Please enter a valid number.")

"""
morse_to_text function converts user's text input into a list of strings by using split.
In this first list are the words of the input. Then, the morse_dict is inverted, so that original keys turn into values
and viceversa; this way, making easier searching for a specific group of dots and underscores.

Inside the for loop, each word is splitted.
It returns another list of strings, but this time, each string represents a letter in Morse code.

Finally, the other for loop goes through each group of dots and underscores and prints their alphanumerical equivalent.
"""

def morse_to_text():
    print("\nNote: This translator uses . and _ for Morse code. While typing your text, separate each letter with a space and each word with a /.")
    text = input("Enter the Morse message to be translated: ")
    words = text.split("/")
    morse_dict_inv = {v: k for k, v in morse_dict.items()}
    for word in words:
        letters = word.split(" ")
        if word != words[0]:
            print(" ", end="")
        for letter in letters:
            print(morse_dict_inv.get(letter, "?"), end="")
    print("\nThe translated text is above.")
    print("")

"""
text_to_morse function splits the string into a list of string (words),
then replaces the blank spaces with a slash "/" with the first for loop.
After that, the nested for loop prints the equivalent in Morse code of each letter.
"""

def text_to_morse():
    text = input("Enter the message to be translated to Morse code: ").upper()
    words = text.split(" ")
    for word in words:
        if word != words[0]:
            print("/", end="")
        for letter in word:
            print(morse_dict.get(letter, "?"), end=" ")
    print("\nThe translated text is above.")
    print("")

"""
text_to_hexadecimal uses a for loop to go through each character in the string,
and gets and prints its equivalent from the hex_dict.
"""

def text_to_hexadecimal():
    text = input("Enter the message to be translated to Hexadecimal: ")
    for letter in text:
        print(hex_dict.get(letter, "?"), end="")
    print("\nThe translated text is above.")
    print("")

"""
hexadecimal_to_text first inverts the hex_dict.
Then, using a for loop goes through the string, but this time,
it creates groups of two characters and stores them temporarily.
Finally, from the inverted hex_dict, the alphanumeric equivalents are obtained and printed.
"""

def hexadecimal_to_text():
    text = input("Enter the message to be translated: ")
    hex_dict_inv = {v: k for k, v in hex_dict.items()}
    for words in range(0, len(text), 2):
        letter = text[words:words + 2]
        print(hex_dict_inv.get(letter, "?"), end="")
    print("\nThe translated text is above.")
    print("")

"""
create_customized_dict allows the user to create its own encryption definitions.
The functions uses a similar menu program that runs infinitely unles the user exits.
When "Add Definitions" is chosen, the user has to type a character and its equivalent in the new system.
Then, the new_dict is updated and printed."""

def create_customized_dict():
    while True:
        print("Welcome to the Encryption System Customizer!")
        print("\n1. Add Definition")
        print("2. Exit")

        try:
            menu_choice = int(input("\nPlease enter your choice (number): "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if menu_choice == 1:
            new_key = input("\nEnter the character: ")
            if len(new_key) == 1:
                new_value = input("Enter the equivalent in the new encryption system: ")
                new_dict.update({new_key: new_value})
                print("The new definition has been added.")
                print(new_dict)
                print("")
            else:
                print("Invalid input. Please enter a single character.\n")
        elif menu_choice == 2:
            break
        else:
            print("Please enter a valid number.")

"""
customized_encryption works simpler than the other encryption function as it depends only on user's definitions.
"""

def customized_encryption():
    text = input("\nEnter the message to be encrypted: ")
    for letter in text:
        print(new_dict.get(letter, "?"), end="")
    print("\nThe translated text is above.")
    print("")

"""
main function is called, which at the same time calls the menu function; thus, starting the whole program.
"""

def main():
    menu()

main()