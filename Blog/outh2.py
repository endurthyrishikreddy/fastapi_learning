from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import Optional, List
from  . import schema, models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from Blog.JWT_token import create_access_token, verify_password
from jose import JWTError
from Blog import schema
import token

oAuth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(db: Session = Depends(get_db), data: str = Depends(oAuth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token.verify_password = verify_password(data)
    

    return 