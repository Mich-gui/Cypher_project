import os
# Compulsory Task 19 - Cypher
# This cypher takes a users entry and encodes the message,
# For every character entered, is changed to the 15th letter after it.
# The cycle starts again after 'z'. i.e. 'z' will become 'o'. This programme
# will leave whitespaces, and punctuations the same as user input.
# The ASCII code for the alphabet uppercase range is 65 and the lowercase range is 97.
# This program then allows the user to save, load or type to screen the encoding process.


def encode_input(cypher_input):  # user_input is the argument
    encoded_input = ""

    for char in cypher_input:
        if char.isalpha():  # isalpha() returns true if the 'char' letters
            # in the user_input is within the alphabet (a-z)
            ascii_offset = 97 if char.islower() else 65
            encoded_char = chr((ord(char) - ascii_offset + 15) % 26 + ascii_offset)
            # % 26 performs the rounds through the alphabet before cycling around again.
            encoded_input += encoded_char
        else:  # the unicode of a specified character i.e. unicode for whitespace is 32.
            encoded_input += char

    return encoded_input


def decode_input(encoded_input):
    decoded_input = ""

    for char in encoded_input:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            decoded_char = chr((ord(char) - ascii_offset - 15) % 26 + ascii_offset)
            decoded_input += decoded_char
        else:
            decoded_input += char

    return decoded_input


def save_file(encoded_input):
    filename = input("Please enter the filename to save your encoded message: ")
    with open(filename, 'a') as file:
        file.write(encoded_input + '\n')
# The user inputs a file name. The function creates the file
# and the encoded word(s) are then written to the txt file.


def load_file():
    filename = input("Enter the name of the text file: ")
    if not os.path.exists(filename):
        print("File could not be found")
        return

    with open(filename, 'r') as file:
        cyphers = file.readlines()
        for cypher in cyphers:
            print(cypher.strip())


def cypher_menu():
    print("""
    -----------------------------------------
    \tWelcome to my cypher programme
    -----------------------------------------
    
    -----------------------------------------
    \tChoose an option from the list:
    -----------------------------------------
    1. Save encoded message(s) to file
    2. Open encoded message(s) file
    3. Encode on screen
    4. Decode messages
    5. Exit
    """)


cypher_menu()
cypher_options = [1, 2, 3, 4, 5]
while True:
    choice = int(input("Enter the option number: "))
    if choice not in cypher_options:
        print("Only enter numerical values from 1 - 5")
        continue

    if choice == 1:
        cypher_input = input("Enter word or sentence to encode: ")
        encoded_input = encode_input(cypher_input)
        save_file(encoded_input)
        cypher_menu()
    elif choice == 2:
        load_file()
        cypher_menu()
    elif choice == 3:
        cypher_input = input("Enter word or sentence to encode: ")
        encoded_input = encode_input(cypher_input)
        print("Encoded input:", encoded_input)
        cypher_menu()
    elif choice == 4:
        cypher_input = input("Enter coded message or sentence to decode: ")
        decoded_input = decode_input(cypher_input)
        print("Decoded input:", decoded_input)
        cypher_menu()
    elif choice == 5:
        exit()
    else:
        continue
