from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
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


@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest):

    #Pseudo
    task = crud.create_translation_task(x, y, p )
    background_task.add_task(perfom_translation, task.id, request.text,request.languages, db)

    return {"task_id": {task.id}}