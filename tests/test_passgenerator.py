import pytest
from app.password_generator import PassGenerator

def test_psw_length():
    passwd = PassGenerator(length=10, upper=True, lower=True, number=True, specialchar=True).generate_psw()
    assert len(passwd) == 10

def test_uppercase():

    uppcase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                "T", "U", "V", "W", "X", "Y", "Z"]
    with_upper = False
    without_upper = False

    psw_with_upper = PassGenerator(length=10, upper=True, lower=True, number=True, specialchar=True).generate_psw()
    psw_without_upper = PassGenerator(length=10, upper=False, lower=True, number=True, specialchar=True).generate_psw()

    for letter in uppcase:
        if letter in psw_with_upper:
            with_upper = True
            break
    
    for letter in uppcase:
        if letter in psw_without_upper:
            without_upper = True
            break 

    assert with_upper == True
    assert without_upper == False

def test_lowercase():

    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z"]

    with_lower = False
    without_lower = False

    psw_with_lower = PassGenerator(length=10, upper=True, lower=True, number=True, specialchar=True).generate_psw()
    psw_without_lower = PassGenerator(length=10, upper=True, lower=False, number=True, specialchar=True).generate_psw()

    for letter in lowercase:
        if letter in psw_with_lower:
            with_lower = True
            break
    
    for letter in lowercase:
        if letter in psw_without_lower:
            without_lower = True
            break 

    assert with_lower == True
    assert without_lower == False

def test_number():

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    with_num = False
    without_num = False

    psw_with_num = PassGenerator(length=10, upper=True, lower=True, number=True, specialchar=True).generate_psw()
    psw_without_num = PassGenerator(length=10, upper=True, lower=True, number=False, specialchar=True).generate_psw()

    for number in numbers:
        if number in psw_with_num:
            with_num = True
            break
    
    for number in numbers:
        if number in psw_without_num:
            without_num = True
            break
    
    assert with_num == True
    assert without_num == False

def test_char():

    characters = ["!", "@", "#", "$", "%", "&", "?","^", "*", "(", ")", "_", "-", "+", "=", "{", "}","[", "]", "|", ":", ";", "<", ">","."]

    with_char = False
    without_char = False

    psw_with_char = PassGenerator(length=10, upper=True, lower=True, number=True, specialchar=True).generate_psw()
    psw_without_char = PassGenerator(length=10, upper=True, lower=True, number=True, specialchar=False).generate_psw()

    for char in characters:
        if char in psw_with_char:
            with_char = True
            break

    for char in characters:
        if char in psw_without_char:
            without_char = True
            break

    assert with_char == True
    assert without_char == False

def test_no_param():
    try:
        no_param = PassGenerator().generate_psw()
        assert False
    except TypeError:
        assert True