from fastapi import APIRouter, Request
from app.main import templates

router = APIRouter()

@router.get("/donaciones")
def donaciones(request: Request):
    return templates.TemplateResponse("donaciones.html", {"request": request})
