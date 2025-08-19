from fastapi import FastAPI

app = FastAPI()

@app.get("/")   
def index():
    return {'data':{'name':'John Doe', 'age':30, 'city':'New York'}}

@app.get("/about")
def about():
    return {'data':"about page"}