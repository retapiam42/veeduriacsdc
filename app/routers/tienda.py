from fastapi import APIRouter, Request, Depends
from app.main import templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.producto import Producto

router = APIRouter()

@router.get("/tienda")
def tienda(request: Request, db: Session = Depends(get_db)):
    productos = db.query(Producto).all()
    return templates.TemplateResponse("tienda.html", {"request": request, "productos": productos})
