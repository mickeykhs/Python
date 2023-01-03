from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def zzang(request: Request):
    return templates.TemplateResponse("zzang3.html", {"request": request})

@app.get("/zzang4", response_class=HTMLResponse)
async def zzang4(request: Request):
    return templates.TemplateResponse("zzang4.html", {"request": request})


    
# uvicorn myajax:app --reload