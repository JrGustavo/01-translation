from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configuración para permitir CORS (si es necesario)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aquí puedes especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Aquí puedes especificar los métodos HTTP permitidos
    allow_headers=["*"],  # Aquí puedes especificar los encabezados permitidos
)

# Configuración para Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get('/index', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
