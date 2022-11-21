
class PassGenerator:
    def __init__(self, length=10, upper=False, lower=False, number=False, specialchar=False) -> None:
        self.length = length
        self.upper = upper
        self.lower = lower
        self.number = number
        self.specialchar = specialchar

    def generate_psw(self):
        pass