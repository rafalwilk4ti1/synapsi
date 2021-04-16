#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
Recruitment Job
Implementation of  ROT47
Written by Rafał Wilk
 14.04.2021

The ROT47 (Caesar cipher by 47 chars) is a simple character substitution cipher that replaces
a character within the ASCII range [33, 126] with the character 47 character after it (rotation)
in the ASCII table. It is an invertible algorithm i.e. applying the same algorithm to the input
twice will get the origin text.
"""

import time
print('Welcome to ROT47 Cipher Code! \n')
print('Or maybe...')
time.sleep(2)
print('(6=4@>6OE@O#~%cfOr:A96COr@56P')


def encode(text, key):
    """Function to decode plain text/sentence"""
    storage = ""  # We create an empty string
    for x in text:
        number = ord(x)  # Iterate text and converting each element to unicode character
        number += key  # Change number value to be equal with rot47
        if number < 32:  # Checking if number is between characters that is used in rot47
            number += 32
        elif number > 126:
            number = (number - 126) + 32
        storage += chr(number)  # Encoded text in string unicode
    return storage


def decode(message, key):
    """Function to decode our encoded text/sentence"""
    storage = ""
    for x in message:  # Iterate text and converting each element to unicode character
        number = ord(x)  # Change number value to be able decode text
        number -= key  # Changing value to normal case sensitive
        if number == 57:
            number = 10
            print(chr(10))
        elif number == 60:
            number = 13
            print(chr(13))
        if number < 32:  # checking value to make sure that our letter will be decoded in good way
            number = 126 - (32 - number)
        storage += chr(number)  # Making string with decoded message

    return storage


def file_open(file_name):
    """Function to open and read files """
    with open(file_name, 'r') as f:  # Opening a file
        text_list = f.read()  # Reading a file
    # string_text = ""  # Creating string
    # for x in text_list:
    #     string_text+=x
    # return string_text
    return text_list


def save_file(file_name, text):
    """ Function to create new file and saved encoded message"""
    with open(file_name, 'w') as f:  # Opening a file
        f.write(text)  # Writing encoded/decoded text
    print('Okey, your message is saved and sound! :D ')
    return text


# Imitation of talk about what we are going to do
run = True
while run:
    message_type = input('\nYou want to use created file or type a normal message(created/normal): ').lower()
    key = 47  # Key is inserted, because in this cipher, user doesn't need to insert for your own

    # Normal typed text
    if message_type.startswith('nor'):
        question_crypt = input('Okej, understood. So, tell me what are you going to do, encode or decode: ').lower()

        # Encode
        if question_crypt.startswith('enc'):
            message = input('What is your message, you want me to encode: ')
            result_message = encode(message, key)  # Encoding process
            print('Here is your encoded message: {}'.format(result_message))  # Show results

        # Decode
        elif question_crypt.startswith('dec'):
            message = input('What will be your message to decode: ')
            result_message = decode(message, key)
            print('Well, it was fun! Let we see if I managed to do it.... \n')
            time.sleep(2)
            print('\nOkey, your decoded code: {}'.format(result_message))
        else:
            print('Guess I did not understand you...')
    # Created file
    elif message_type.startswith('cre'):  # It works if user choose created file
        file_name = input('Well, I am going to need a name of your file: ')  # Load the file name
        question_crypt = input('Roger that. \n\n Let me know what you prefer today, encode or decode:  ').lower()

        # Encode
        if question_crypt.startswith('enc'):  # Works if user choose enc
            text_list = file_open(file_name)  # Run file_open function
            result_message = encode(text_list, key)  # Encoding process
            print('\nHere is your encoded message: {}'.format(result_message))  # Show results
            saved = input('\nWould you like to save your message in a new file? (y/n)')
            if saved.startswith('y'):
                name = input('How would you like to name your file? ')  # Name your saving file
                save_file(name, result_message)  # Saving file
            else:
                pass
        # Decode
        elif question_crypt.startswith('dec'):  # It works if user want to decode text
            text_list = file_open(file_name)  # run file_open function
            result_message = decode(text_list, key)  # Decoding process
            print('Well, it was fun! Let we see if I managed to do it.... \n')
            time.sleep(2)
            print('\nOkey, your decoded code: {}'.format(result_message))
            saved = input('\nWould you like to save your message in a new file? (y/n)')
            if saved.startswith('y'):
                name = input('How would you like to name your file? ')  # Name your saving file
                save_file(name, result_message)  # Saving file
            else:
                pass

    else:
        print("You probably wrote something invalid...")

    # Ending the program
    rerun = input('\nWould you like me to do something else:? ').lower()
    if rerun.startswith('y'):
        run = True
    elif rerun.startswith('n'):
        print('Okay, thanks for today. See you next time.')
        time.sleep(3)
        print("\n \t TOP -> xOH:==O36OJ@FCO36DEOAC@8C2>>6C]Ox7OJ@FO9:C6O>6OxO2>OC625JOE@ODA6?5O2==O>JOE:>6OE@O:>AC@G6O>JOD"
              "<:==O2?5O36O36EE6CO52JO27E6CO52J]OiX <-SECRET ?")
        run = False
