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

class ShowBlog(page):
    title: str
    content: str
    creator : ShowUser

    class Config:
        orm_mode = True    
      