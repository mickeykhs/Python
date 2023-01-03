from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
@app.get("/threejs", response_class=HTMLResponse)
async def threejs(request: Request):
    return templates.TemplateResponse("threejs.html", {"request": request})

    
# uvicorn mythreejs:app --reload