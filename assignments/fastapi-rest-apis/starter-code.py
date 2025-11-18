from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Item Management API", version="1.0.0")

# Pydantic model for Item
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

# In-memory storage for items
items_db: List[Item] = []
next_id = 1

# TODO: Implement the following endpoints:

# GET /items - Retrieve all items
# GET /items/{item_id} - Retrieve a specific item by ID
# POST /items - Create a new item
# PUT /items/{item_id} - Update an existing item
# DELETE /items/{item_id} - Delete an item

# Example endpoint to get you started:
@app.get("/items", response_model=List[Item])
def get_items():
    """
    Retrieve all items from the database.
    
    Returns:
        List of all items currently stored
    """
    return items_db

# Add more endpoints below...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
