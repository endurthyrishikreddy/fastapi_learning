from pydantic import BaseModel

class page(BaseModel):
    title: str
    content: str
    #published: bool = True  
    class Config:
        orm_mode = True 



class User(BaseModel):
    username: str
    email: str
    password: str

class ShowUser(BaseModel):
    username: str
    email: str
    #password: str
    blogs: list[page] = []

    class Config:
        orm_mode = True      


from typing import Optional

class ShowBlog(page):
    title: str
    content: str
    creator: Optional[ShowUser] = None

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True 

class Token(BaseModel):
    access_token: str
    token_type: str 

class TokenData(BaseModel):
    username: str

    class Config:
        orm_mode = True    