from fastapi import FastAPI
import schemas

from passgen import PassGenerator

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/password/", response_model=schemas.Password)
async def get_password():
    generator = PassGenerator()
    passwd = generator.generate_psw()
    return {"password": passwd}