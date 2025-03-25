from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database import Base
from sqlalchemy.orm import relationship


class TbcSucursales(Base):
    __tablename__ = 'tbc_sucursales'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(60), nullable=False)
    Direccion = Column(String(150), nullable=False)
    Responsable_ID = Column(Integer, ForeignKey('tbb_personas.ID'), nullable=True)  # Relación con tbb_personas
    Total_Clientes_Atendidos = Column(Integer, nullable=True, default=0)
    Promedio_Clientes_X_Dia = Column(Integer, nullable=True, default=0)
    Capacidad_Maxima = Column(Integer, nullable=True)
    Total_Empleados = Column(Integer, nullable=True, default=0)
    Horario_ID = Column(Integer, ForeignKey('tbb_horarios.ID'), nullable=True)  # Relación con tbb_horarios
    Estatus = Column(Boolean, default=True)
    Fecha_Registro = Column(DateTime, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

        # Relación con TbbPersonas (Responsable)
    responsable = relationship('TbbPersonas', backref='sucursales')

    # Relación con TbbHorarios
    horario = relationship('TbbHorarios', backref='sucursales')
