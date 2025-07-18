from fastapi import APIRouter, Request, Depends, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.denuncia import Denuncia
from app.main import templates

router = APIRouter()

@router.get("/denuncias", response_class=HTMLResponse)
async def denuncias(request: Request):
    return templates.TemplateResponse("denuncias.html", {"request": request})

@router.post("/denuncias")
async def crear_denuncia(
    request: Request,
    db: Session = Depends(get_db),
    titulo: str = Form(...),
    descripcion: str = Form(...),
    archivo: UploadFile = File(None)
):
    error_message = None
    success_message = None
    
    try:
        archivo_data = None
        if archivo:
            # Validar tipo de archivo si es necesario
            if not archivo.content_type.startswith("image/"):
                raise ValueError("El archivo debe ser una imagen.")
            
            archivo_data = await archivo.read()

        nueva_denuncia = Denuncia(
            titulo=titulo,
            descripcion=descripcion,
            archivo=archivo_data
        )
        db.add(nueva_denuncia)
        db.commit()
        success_message = "Denuncia enviada con éxito."
        
    except ValueError as e:
        error_message = str(e)
    except Exception as e:
        error_message = f"Error al procesar la denuncia: {e}"
        db.rollback()

    return templates.TemplateResponse(
        "denuncias.html",
        {
            "request": request,
            "error_message": error_message,
            "success_message": success_message,
        },
    )
