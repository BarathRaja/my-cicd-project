import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

DB_PASSWORD = os.getenv("TEST_DB_PASSWORD")

@app.get("/")
def read_root():
    return {"message": "Hello Docker"}

@app.post("/items/")
def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")
    return {"item_name": item.name, "price": item.price}

@app.get("/secure-data/")
def get_secure_data():
    if DB_PASSWORD == "super_secret_123":
        return {"data": "Top secret information"}
    raise HTTPException(status_code=401, detail="Unauthorized")
