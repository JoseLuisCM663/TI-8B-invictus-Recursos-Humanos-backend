from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database import Base


class TbcSucursales(Base):
    __tablename__ = 'tbc_sucursales'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(60), nullable=False)
    Direccion = Column(String(150), nullable=False)
    Responsable_ID = Column(Integer)  # Suponiendo que Responsable_ID tiene una relación
    Total_Clientes_Atendidos = Column(Integer, nullable=True, default=0)
    Promedio_Clientes_X_Dia = Column(Integer, nullable=True, default=0)
    Capacidad_Maxima = Column(Integer, nullable=True)
    Total_Empleados = Column(Integer, nullable=True, default=0)
    Horario_ID = Column(Integer)  # Suponiendo relación con una tabla Horarios
    Estatus = Column(Boolean, default=True)
    Fecha_Registro = Column(DateTime, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
