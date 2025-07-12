from fastapi import APIRouter, Request
from app.main import templates

router = APIRouter()

@router.get("/denuncias")
def denuncias(request: Request):
    return templates.TemplateResponse("denuncias.html", {"request": request})
