from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/blog")   
def index(limit:Optional[int] = 10 , published: Optional[bool] = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blog index"}
    else:
        return {"data": f"{limit} blog index"}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'This is an unpublished blog post.'}

@app.get("/blog/{id}")
def about(id: int):
    return {'data': id}

@app.get("/blog/{id}/comments")
def comments(id: int):
    if( id == 0):
        return {'data': 'No comments available for this blog post.'}
    return {'data': [{'comment_id': 1, 'content': 'Great post!'}, {'comment_id': 2, 'content': 'Thanks for sharing!'}]} 



class Blog(BaseModel):
    title: str
    content: str
    published: bool = True


@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"{request.title} Blog created successfully."}