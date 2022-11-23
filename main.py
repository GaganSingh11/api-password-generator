from fastapi import FastAPI, Request
from typing import Optional
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
import schemas
from password_generator import PassGenerator

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
def resource_not_found(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"details": "Invalid resource URI"}
    )

@app.get("/api/v1/password", response_model=schemas.Password, tags=["Generate Password"], description="Generate random password based on selection")
async def get_password(
                    pwd_length: Optional[int] = 10,
                    uppercase: Optional[bool] = False,
                    lowercase: Optional[bool] = False,
                    number: Optional[bool] = False,
                    special_char: Optional[bool] = False 
                ):

    generator = PassGenerator(pwd_length,uppercase, lowercase, number, special_char)
    passwd = generator.generate_psw()
    return {"password": passwd}