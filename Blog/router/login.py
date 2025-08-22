from fastapi import APIRouter
from typing import List , Optional
from fastapi import Depends, status, Response, HTTPException
from .. import schema, models
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from Blog.JWT_token import create_access_token

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("")
def login(request : OAuth2PasswordRequestForm  = Depends(),db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not pwd_context.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

    return {"message": "Login successful", "user_id": user.id, "username": user.username}