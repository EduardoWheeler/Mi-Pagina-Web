from sqlalchemy import Column, Integer, String
from database import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    contrasenia = Column(String(100), nullable=False)