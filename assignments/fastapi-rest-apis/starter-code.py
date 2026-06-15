from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items = {}
next_id = 1

@app.get("/items")
def list_items(q: Optional[str] = None):
    if q:
        return [item for item in items.values() if q.lower() in item["name"].lower()]
    return list(items.values())

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items")
def create_item(item: Item):
    global next_id
    item_data = item.dict()
    item_data["id"] = next_id
    items[next_id] = item_data
    next_id += 1
    return item_data

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items.pop(item_id)

# Execute localmente com:
# uvicorn assignments.fastapi-rest-apis.starter-code:app --reload
# Depois acesse http://127.0.0.1:8000/docs para ver a documentação automática.
