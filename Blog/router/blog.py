from fastapi import APIRouter
from fastapi import Depends, status, Response, HTTPException
from typing import Optional, List
from .. import schema, models
from ..database import engine, SessionLocal , get_db
from sqlalchemy.orm import Session 


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

# get_db = get_db

@router.get("", status_code=status.HTTP_200_OK, response_model=List[schema.ShowBlog])
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post("", status_code=status.HTTP_201_CREATED)
def create_blog(request: schema.page, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, content=request.content , user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

@router.get("/{id}" , status_code=status.HTTP_200_OK, response_model=schema.ShowBlog)
def show(id: int,response :Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first(    )
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    db.delete(blog)
    db.commit()
    return {"detail": f"Blog deleted successfully  {blog}"}

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED , response_model=schema.ShowBlog)
def update(id: int, request: schema.page, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.title = request.title
    blog.content = request.content
    db.commit()
    db.refresh(blog)
    return blog

