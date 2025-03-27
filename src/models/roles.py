from sqlalchemy import Column, Integer, String, DateTime,Text,Boolean
from database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Roles(Base):
    __tablename__ = "tbc_roles"

    ID = Column(Integer,primary_key=True,autoincrement=True,index=True)
    Nombre = Column(String(60),unique=True,index=True)
    Descripcion = Column(Text, nullable=True)
    Estatus = Column(Boolean, default=True)
    Fecha_Registro = Column(DateTime, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)