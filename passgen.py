import random

class PassGenerator:
    def __init__(self, length=10, upper=False, lower=False, number=False, specialchar=False) -> None:
        self.length = length
        self.upper = upper
        self.lower = lower
        self.number = number
        self.specialchar = specialchar

    def generate_psw(self):
        collection = {
            'uppercase': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                          'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],

            'lowercase': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z'],

            'numbers': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

            'special_char': ['!', '@', '#', '$', '%', '&', '?','^', '*', '(', ')', '_', '-', '+', '=', '{', '}','[', ']', '|', ':', ';', '<', '>','.']
        }

        choices = []

        if self.upper:
            choices.extend(collection['uppercase'])
        if self.lower:
            choices.extend(collection['lowercase'])
        if self.number:
            choices.extend(collection['numbers'])
        if self.specialchar:
            choices.extend(collection['special_char'])
        

        passwd = ''
        for element in range(self.length):
            passwd = passwd + random.choice(choices)

        return passwd



if __name__ == '__main__':
    passwd = PassGenerator(upper=True, lower=True, number=True, specialchar=True).generate_psw()
    print(passwd)