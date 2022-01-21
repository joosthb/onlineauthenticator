from typing import Optional, List
from fastapi import File, UploadFile, FastAPI
# for QR image parsing
from pyzbar.pyzbar import decode
from PIL import Image

# for totp generation
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

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    # extract qr data
    contents = await file.read()
    # save_file(file.filename, contents)
    qrdata += decode(Image.frombytes(contents))
    return {"qr_data": qrdata}