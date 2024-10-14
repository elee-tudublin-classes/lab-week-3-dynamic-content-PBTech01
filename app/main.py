from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import httpx
from contextlib import asynccontextmanager
import json
from starlette.config import Config

# Load environment variables from .env
config = Config(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.requests_client = httpx.AsyncClient()
    yield
    await app.requests_client.aclose()


# create app instance
app = FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory="app/view_templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return templates.TemplateResponse("index.html", {"request": request, "serverTime": server_time})

@app.get("/advice", response_class=HTMLResponse)
async def advice(request: Request):
    
    # Define a request_client instance
    requests_client = request.app.requests_client

    # Connect to the API URL and await the response
    response = await requests_client.get(config("ADVICE_URL"))

    # Send the json data from the response in the TemplateResponse data parameter 
    return templates.TemplateResponse("advice.html", {"request": request, "data": response.json() })

@app.get("/apod", response_class=HTMLResponse)
async def apod(request: Request):
    
    # Define a request_client instance
    requests_client = request.app.requests_client

    # Connect to the API URL and await the response
    response = await requests_client.get(config("NASA_APOD_URL") + config("NASA_API_KEY"))
    print(response)
    # Send the json data from the response in the TemplateResponse data parameter 
    return templates.TemplateResponse("apod.html", {"request": request, "data": response.json() })


app.mount("/static", StaticFiles(directory="app/static"), name="static")

