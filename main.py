from fastapi import FastAPI, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,HTMLResponse
from pydantic import EmailStr
from deta import Deta
from typing import Optional


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

deta = Deta()

@app.get('/', response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse('index.html', {'request': request})

#@app.get('/gallery', response_class=HTMLResponse)
#def index(request:Request):
#    return templates.TemplateResponse('gallery.html', {'request': request})