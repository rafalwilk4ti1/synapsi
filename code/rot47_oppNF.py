# import sys
import click

#
# @click.command()
# @click.option('-option', help='Choose encode or decode')
# @click.option('-message', help='Message or file you want to cipher')

@click.command()
@click.option('-option', help='Choose encode or decode')
@click.option('-message', help='Message or file you want to cipher')
class Configuration:

    def __init__(self, option, message):
        self.message = option
        self.option = message


class Rot(Configuration):

    def __init__(self, message, option):
        super(Rot, self).__init__(message, option)
        # self.message = ''
        # self.choice = ''
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
        # click.echo(self.encoded_message)

    def decode(self):
        for x in self.message:
            self.number = ord(x)
            self.number -= self.key
            if self.number < 32:
                self.number = 126 - (32 - self.number)
            self.decoded_message += chr(self.number)

        print(self.decoded_message)
        # click.echo(self.decoded_message)


config = Configuration()
game = Rot(config)
