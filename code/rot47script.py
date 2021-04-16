def encode(text, key=47):
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


def decode(message, key=47):
    """Function to decode our encoded text/sentence"""
    storage = ""
    for x in message:  # Iterate text and converting each element to unicode character
        number = ord(x)  # Change number value to be able decode text
        number -= key  # Changing value to normal case sensitive
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
    return text
