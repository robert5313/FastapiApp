from pydantic import BaseModel, EmailStr

class User(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phone: int
    password: str