from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, World!"})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None, k: str = None):
    return {"item_id": item_id, "q": q, "k": k}
