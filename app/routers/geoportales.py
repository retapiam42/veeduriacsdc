from fastapi import APIRouter, Request
from app.main import templates

router = APIRouter()

@router.get("/geoportales")
def geoportales(request: Request):
    return templates.TemplateResponse("geoportales.html", {"request": request})
