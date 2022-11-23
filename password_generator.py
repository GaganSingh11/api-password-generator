import random

class PassGenerator:
    def __init__(self, length, upper, lower, number, specialchar) -> None:
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

        pool = []

        if self.upper:
            pool.extend(collection['uppercase'])
        if self.lower:
            pool.extend(collection['lowercase'])
        if self.number:
            pool.extend(collection['numbers'])
        if self.specialchar:
            pool.extend(collection['special_char'])

        passwd = ''
        if not self.upper and not self.lower and not self.number and not self.specialchar:
            passwd = "very&unsafe&password"
        else:
            for _ in range(self.length):
                passwd = passwd + random.choice(pool)

        return passwd


if __name__ == '__main__':
    passwd = PassGenerator().generate_psw()
    print(passwd)