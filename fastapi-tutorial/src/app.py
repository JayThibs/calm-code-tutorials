from fastapi import FastAPI
from .pydantic_models import Item

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}


@app.post("/items/")
def create_item(item: Item):
    return item
