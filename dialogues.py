#https://py.checkio.org/ru/mission/dialogues/
#OOP
#Dialogues

VOWELS = "aeiou"

class Chat:

    def __init__(self):
        self.human_dialogue = []
        self.robot_dialogue = []

    def connect_human(self, human):
        human.chat = self

    def connect_robot(self, robot):
        robot.chat = self

    def show_human_dialogue(self):
        return '\n'.join(self.human_dialogue)

    def show_robot_dialogue(self):
        return '\n'.join(self.robot_dialogue)


class Human:
    def __init__(self, name):
        self.name = name
        self.chat = []

    def send(self, message):
        self.chat.human_dialogue.append(f'{self.name} said: {message}')
        self.chat.robot_dialogue.append(f'{self.name} said: ' + ''.join([(lambda i: '0' if i in VOWELS else '1')(i) for i in message]))

class Robot:
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def send(self, message):
        self.chat.human_dialogue.append(f'{self.serial_number} said: {message}')
        self.chat.robot_dialogue.append(f'{self.serial_number} said: ' + ''.join([(lambda i: '0' if i in VOWELS else '1')(i) for i in message]))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")