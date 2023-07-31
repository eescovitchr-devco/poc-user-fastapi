from pydantic import BaseModel
from pydantic import EmailStr

class User(BaseModel):
    email: EmailStr
    organization: str