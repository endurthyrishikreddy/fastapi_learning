from fastapi import FastAPI , Depends , status , Response , HTTPException
from typing import Optional , List

from . import schema,models
from .database import engine , SessionLocal , get_db
from sqlalchemy.orm import Session, joinedload
from passlib.context import CryptContext
from .router import blog , user , login 



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)

# Example: Use joinedload when querying blogs to ensure creator is loaded
# from sqlalchemy.orm import joinedload
# blogs = db.query(models.Blog).options(joinedload(models.Blog.creator)).all()





