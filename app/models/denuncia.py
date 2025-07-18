from sqlalchemy import Column, Integer, String, LargeBinary
from app.database import Base

class Denuncia(Base):
    __tablename__ = "denuncias"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descripcion = Column(String)
    archivo = Column(LargeBinary)

