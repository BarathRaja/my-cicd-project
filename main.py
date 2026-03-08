import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Hello Master Surya"}

@app.post("/items/")
def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")
    return {"item_name": item.name, "price": item.price}

@app.get("/secure-data/")
def get_secure_data():
    # Fetch the environment variable dynamically on every request
    db_password = os.getenv("TEST_DB_PASSWORD")
    
    if db_password == "super_secret_123":
        return {"data": "Top secret information"}
    raise HTTPException(status_code=401, detail="Unauthorized")
