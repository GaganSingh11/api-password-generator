from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 404

def test_non_existing_path():
    response = client.get("/non/exisiting/path")
    assert response.status_code == 404

def test_no_flag():
    response = client.get("/api/v1/password")
    assert response.status_code == 406
    assert response.json() == {"detail": "Switch on atleast one flag from uppercase, lowercase, number or special_char"}

def test_psw_length_limit():
    response = client.get("/api/v1/password?pwd_length=201&number=true")
    assert response.status_code == 406
    assert response.json() == {"detail": "Password length exceeded limit of 200"}

def test_psw_default_length():
    response = client.get("/api/v1/password?number=true")
    psw = response.json()
    assert len(psw["password"]) == 10

def test_flag_effectivness():
    response = client.get("/api/v1/password?uppercase=true&lowercase=true&number=true&special_char=true")

    psw = response.json()
    psw_string = psw["password"]

    upper, lower, number, char = False, False, False, False
    for item in psw_string:
        if item in "abcdefghijklmnopqrstuvwxyz":
            lower = True
        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper = True
        if item in "0123456789":
            number = True
        if item in "!@#$%&?^*()_-+={}[]|:;<>.":
            char = True

    assert upper == True
    assert lower == True
    assert number == True
    assert char == True
