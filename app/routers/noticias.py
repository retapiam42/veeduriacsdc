from fastapi import APIRouter, Request
from app.main import templates

router = APIRouter()

@router.get("/noticias")
def noticias(request: Request):
    return templates.TemplateResponse("noticias.html", {"request": request})
