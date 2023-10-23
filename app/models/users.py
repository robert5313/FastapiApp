from pydantic import BaseModel

class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: int
    password: str