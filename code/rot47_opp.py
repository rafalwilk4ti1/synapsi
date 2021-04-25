import sys


class Rot:

    def __init__(self):
        self.message = ''
        self.choice = ''
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

        print(self.encoded_message)

    def decode(self):
        for x in self.message:
            self.number = ord(x)
            self.number -= self.key
            if self.number < 32:
                self.number = 126 - (32 - self.number)
            self.decoded_message += chr(self.number)

        print(self.decoded_message)

    def play(self):
        while self.run:
            self.encoded_message = ""
            self.decoded_message = ""
            self.message = input('What is your message: ')
            self.choice = input('What are you going to do (encode/decode): ')

            if self.choice.startswith('en'):
                self.encode()
            elif self.choice.startswith('de'):
                self.decode()
            else:
                print("You're wrong try again... later :x")

            self.again = input('\nDo you want to use us me again: ')
            if self.again.startswith('y'):
                self.run = True
            else:
                print('Well see you later, then. ')
                self.run = False
                sys.exit()


game = Rot()
game.play()
