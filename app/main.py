from typing import Optional
from fastapi import FastAPI
import mintotp

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/code/{shared_key}")
async def read_item(shared_key: str):
    return {"current_code": mintotp.totp(shared_key)}
