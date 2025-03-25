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
    Persona_ID = Column(Integer)  # Relación opcional con otra tabla
    Descripcion = Column(Text, nullable=False)  # Campo obligatorio
    Tipo = Column(Enum(TipoQueja), nullable=False, default="sugerencia")  # Campo obligatorio
    Respuesta = Column(Text, nullable=True)  # Puede estar vacío inicialmente
    Estatus = Column(Enum(EstatusQueja), nullable=False, default="espera")
    Fecha_registro = Column(DateTime, nullable=False)
    Fecha_actualizacion = Column(DateTime, nullable=False)
