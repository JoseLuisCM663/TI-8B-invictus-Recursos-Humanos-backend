from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey, Enum
from database import Base
from datetime import datetime
import enum

class TipoQueja(enum.Enum):
    sugerencia = "sugerencia"
    queja = "queja"
    reclamo = "reclamo"

class EstatusQueja(enum.Enum):
    respondida = "respondida"
    espera = "espera"
    archivada = "archivada"

class QuejasSugerencias(Base):
    __tablename__ = "tbd_quejas_sugerencias"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Id_persona = Column(Integer)  # Relación opcional con otra tabla
    descripcion = Column(Text, nullable=False)  # Campo obligatorio
    tipo = Column(Enum(TipoQueja), nullable=False, default="sugerencia")  # Campo obligatorio
    respuesta = Column(Text, nullable=True)  # Puede estar vacío inicialmente
    estatus = Column(Enum(EstatusQueja), nullable=False, default="espera")
    fecha_registro = Column(DateTime, nullable=False)
    fecha_actualizacion = Column(DateTime, nullable=False)
