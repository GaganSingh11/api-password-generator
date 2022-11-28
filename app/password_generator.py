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
            "uppercase": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                          "T", "U", "V", "W", "X", "Y", "Z"],

            "lowercase": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                          "t", "u", "v", "w", "x", "y", "z"],

            "numbers": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],

            "special_char": ["!", "@", "#", "$", "%", "&", "?","^", "*", "(", ")", "_", "-", "+", "=", "{", "}","[", "]", "|", ":", ";", "<", ">","."]
        }

        pool = []

        if self.upper:
            pool.extend(collection["uppercase"])
        if self.lower:
            pool.extend(collection["lowercase"])
        if self.number:
            pool.extend(collection["numbers"])
        if self.specialchar:
            pool.extend(collection["special_char"])

        while True:

            passwd = ""
            for _ in range(self.length):
                random.shuffle(pool)
                passwd = passwd + random.choice(pool)

            constraint = []
            if self.upper:
                constraint.append(any(char in collection["uppercase"] for char in passwd))
            if self.lower:
                constraint.append(any(char in collection["lowercase"] for char in passwd))
            if self.number:
                constraint.append(any(char in collection["numbers"] for char in passwd))
            if self.specialchar:
                constraint.append(any(char in collection["special_char"] for char in passwd))
  
            
            if len(set(constraint)) == 1:
                break

        return passwd


if __name__ == "__main__":
    passwd = PassGenerator(length=10, upper=True, lower=True, number=True, specialchar=True).generate_psw()
    print(passwd)