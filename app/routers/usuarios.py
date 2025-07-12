from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User

router = APIRouter()

@router.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = next(get_db())):
    user = db.query(User).filter(User.username == username).first()
    if user:
        return RedirectResponse("/", status_code=303)
    return RedirectResponse("/login", status_code=303)
