from typing import Optional, List
from fastapi import File, UploadFile, FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from time import time

# for totp generation
import mintotp

# for QR image parsing
# from pyzbar.pyzbar import decode
# from PIL import Image


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/totp/{shared_key}", response_class=HTMLResponse)
async def read_item(request: Request, shared_key: str):
    validity = 30 - int(time())%30
    try:
      totp = mintotp.totp(shared_key)
    except:
      totp = None
    return templates.TemplateResponse("item.html", {"request": request, "totp": totp, "validity": validity})

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.post("/upload")
# async def upload(file: UploadFile = File(...)):
#     # extract qr data
#     contents = await file.read()
#     # save_file(file.filename, contents)
#     qrdata = decode(Image.frombytes(contents))
#     return {"qr_data": qrdata}