from fastapi import FastAPI , Depends , status , Response , HTTPException
from typing import Optional , List
from . import schema,models
from .database import engine , SessionLocal , get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .router import blog , user 


app = FastAPI()

models.Base.metadata.create_all(bind=engine) 

app.include_router(blog.router)
app.include_router(user.router)





