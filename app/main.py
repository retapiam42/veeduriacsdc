"""from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def leer_root():
    return {"mensaje": "soy rafael tapia morales"}
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import (
    index,
    proyectos,
    denuncias,
    transparencia,
    donaciones,
    noticias,
    contacto,
    geoportales,
    usuarios,
    tienda,
    carrito
)
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")
# Rutas
app.include_router(index.router)
app.include_router(proyectos.router)
app.include_router(denuncias.router)
app.include_router(transparencia.router)
app.include_router(donaciones.router)
app.include_router(noticias.router)
app.include_router(contacto.router)
app.include_router(geoportales.router)
app.include_router(usuarios.router)
app.include_router(tienda.router)
app.include_router(carrito.router)