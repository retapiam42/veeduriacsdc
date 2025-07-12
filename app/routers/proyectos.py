from fastapi import APIRouter, Request
from app.main import templates

router = APIRouter()

@router.get("/proyectos")
def proyectos(request: Request):
    return templates.TemplateResponse("proyectos.html", {"request": request})
