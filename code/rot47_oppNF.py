import click


class Rot:

    def __init__(self, option, message):
        self.message = message
        self.choice = option
        self.encoded_message = ""
        self.decoded_message = ""
        self.key = 47
        self.number = 0
        self.run = True
        self.again = ''

    def encode(self):
        for x in self.message:
            self.number = ord(x)
            self.number += self.key
            if self.number < 32:
                self.number += 32
            elif self.number > 126:
                self.number = (self.number - 126) + 32
            self.encoded_message += chr(self.number)

        return self.encoded_message

    def decode(self):
        for x in self.message:
            self.number = ord(x)
            self.number -= self.key
            if self.number < 32:
                self.number = 126 - (32 - self.number)
            self.decoded_message += chr(self.number)

        return self.decoded_message


class FileOperator:

    cipher_text = ''

    def __init__(self, file_name):
        self.file_name = file_name
        self.read_list = ''

    def read_file(self):
        with open(self.file_name, 'r') as f:
            read_list = f.read()
        return read_list

    def save_file(self, cipher_text):
        with open(self.file_name, 'w') as f:
            f.write(cipher_text)
        return self.file_name


@click.command()
@click.argument('option')
@click.argument('message')
def configuration(option, message):
    game = Rot(option, message)
    if message.endswith('.txt'):
        game_file = FileOperator(message)
        new_message = game_file.read_file()
        game_2 = Rot(option, new_message)

        if option.startswith('en'):
            cipher_message = game_2.encode()
            game_file.save_file(cipher_message)
        elif option.startswith('de'):
            cipher_message = game_2.decode()
            game_file.save_file(cipher_message)
    else:
        if option.startswith('en'):
            print(game.encode())
        elif option.startswith('de'):
            print(game.decode())
        else:
            print('You wrote sth wrong...')


if __name__ == '__main__':
    configuration()

