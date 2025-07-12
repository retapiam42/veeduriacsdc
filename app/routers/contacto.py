from fastapi import APIRouter, Request
from app.main import templates

router = APIRouter()

@router.get("/contacto")
def contacto(request: Request):
    return templates.TemplateResponse("contacto.html", {"request": request})
