from fastapi import FastAPI
from pyzbar.pyzbar import decode
from io import BytesIO
from PIL import Image
import base64

app = FastAPI()

@app.get("/decode")
async def root(qr: str = ''):
    b = BytesIO(base64.b64decode(qr))
    image = Image.open(b, formats=['PNG'])
    decode_image = decode(image)
    result = list(map(lambda e: e[0].decode('utf-8'), decode_image))
    return {'result': result }


