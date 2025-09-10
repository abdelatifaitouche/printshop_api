from pydantic import BaseModel , Field




class UserBase(BaseModel):
    id : str
    username : str
    email : str
    role : str



class CreateUser(BaseModel):
    username : str = Field(min_length=6)
    email : str
    password_hash : str = Field(min_length=8)
    role : str


class UserLogin(BaseModel):
    email : str
    password_hash : str


