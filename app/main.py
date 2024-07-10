from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
import schemas
import crud
import models
from database import get_db, engine 

models.Base.metadata.create_all(bind=engine)
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


@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest):

    #pseudo
    task = crud.create_translation_task(get_db.db, request.text, request.languages)

    background_tasks.add_task(perfom_translation, task.id, request.text, request.languages, get_db.db)

    return {"task_id": {task.id}}