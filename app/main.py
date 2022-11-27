from fastapi import FastAPI, HTTPException, status
from typing import Optional
import app.schemas as schemas
from app.password_generator import PassGenerator

PASSWORD_LENGTH_LIMIT = 200

app = FastAPI(
    title="Password on Demand",
    description="Generate random password based on selected flags")


@app.get("/api/v1/password", response_model=schemas.Password, tags=["Generate Password"], description="Generate password based on selection")
async def get_password(pwd_length: Optional[int] = 10,
                uppercase: Optional[bool] = False,
                lowercase: Optional[bool] = False,
                number: Optional[bool] = False,
                special_char: Optional[bool] = False):

    if not uppercase and not lowercase and not number and not special_char:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, 
                    detail="Switch atleast one flag from uppercase, lowercase, number or special_char")

    if pwd_length > PASSWORD_LENGTH_LIMIT:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, 
                    detail=f"Password length exceeded limit of {PASSWORD_LENGTH_LIMIT}")

    generator = PassGenerator(pwd_length,uppercase, lowercase, number, special_char)
    passwd = generator.generate_psw()
    return {"password": passwd}