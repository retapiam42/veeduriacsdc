from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from app.main import templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import carrito as carrito_model

router = APIRouter()

@router.post("/carrito/add/{producto_id}")
def add_to_cart(producto_id: int, db: Session = Depends(get_db)):
    item = carrito_model.Carrito(user_id=1, producto_id=producto_id, cantidad=1)
    db.add(item)
    db.commit()
    return RedirectResponse(url="/tienda", status_code=303)

@router.get("/carrito")
def view_cart(request: Request, db: Session = Depends(get_db)):
    items = db.query(carrito_model.Carrito).filter(carrito_model.Carrito.user_id == 1).all()
    return templates.TemplateResponse("carrito.html", {"request": request, "items": items})
