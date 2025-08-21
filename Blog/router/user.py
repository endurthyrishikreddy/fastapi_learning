from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import Optional, List 
from .. import schema, models
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext



router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("", status_code=status.HTTP_201_CREATED , response_model=schema.ShowUser)
def create_user(request: schema.User, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_user = models.User(username=request.username, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user 