from fastapi import APIRouter, Request
from app.main import templates

router = APIRouter()

@router.get("/transparencia")
def transparencia(request: Request):
    return templates.TemplateResponse("transparencia.html", {"request": request})
