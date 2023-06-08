from pydantic import BaseModel
from typing import Union



class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str


class User(UserBase):
    id: int


class AccessToken(BaseModel):
    access_token: str

class Token(AccessToken):
    refresh_token: str

class UserInDB(User):
    hashed_password: str


class RegisterJson(BaseModel):
    """
    """
    username: str
    email: Union[str, None] = None
    password: str


class LoginJson(BaseModel):
    """
    """
    username: str
    password: str