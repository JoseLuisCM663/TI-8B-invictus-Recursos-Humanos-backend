from sqlalchemy import Column, Integer, String, Date, Enum, Boolean, DateTime
from datetime import datetime
import enum
from database import Base


# Definimos los enums para Genero y Tipo_Sangre
class Genero(enum.Enum):
    M = 'M'
    H = 'H'
    NB = 'N/B'

class TipoSangre(enum.Enum):
    A_pos = 'A+'
    A_neg = 'A-'
    B_pos = 'B+'
    B_neg = 'B-'
    AB_pos = 'AB+'
    AB_neg = 'AB-'
    O_pos = 'O+'
    O_neg = 'O-'

class TbbPersonas(Base):
    __tablename__ = 'tbb_personas'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Titulo_Cortesia = Column(String(20), nullable=True)
    Nombre = Column(String(80), nullable=False)
    Primer_Apellido = Column(String(80), nullable=False)
    Segundo_Apellido = Column(String(80), nullable=True)
    Fecha_Nacimiento = Column(Date, nullable=False)
    Fotografia = Column(String(100), nullable=True)
    Genero = Column(Enum(Genero), nullable=False)
    Tipo_Sangre = Column(Enum(TipoSangre), nullable=False)
    Estatus = Column(Boolean, default=True)
    Fecha_Registro = Column(DateTime, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

