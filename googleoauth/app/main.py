from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app=FastAPI()
templetes=Jinja2Templates(directory='templates')

@app.get("/")
def index(request:Request):
    return templetes.TemplateResponse(
        name="index.html",
        context={"request":request}
    )