from app.password_generator import PassGenerator

def test_generate_pass():
    passwd = PassGenerator(length=10, upper=True, lower=True, number=True, specialchar=True).generate_psw()
    assert len(passwd) == 10    