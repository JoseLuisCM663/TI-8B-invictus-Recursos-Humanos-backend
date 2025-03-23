from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Colaborador(Base):
    __tablename__ = "tbb_colaboradores"
    
    ID = Column(Integer, primary_key=True, autoincrement=True, index=True)
    Nombre= Column(String(50))
    Persona_Id = Column(Integer,unique=True)
    Sucursal_Id = Column(Integer)
    Servicio_Id = Column(Integer)
    Correo_Electronico = Column(String(100), unique=True, index=True)
    Especialidad = Column(String(50), nullable=True)
    Numero_Telefonico_Movil = Column(String(20), nullable=True)
    Estatus = Column(Boolean, default=True)  # 1 para 'activo', 0 para 'inactivo'
    Fecha_Registro = Column(DateTime, nullable=False)
    Fecha_Actualizacion = Column(DateTime, nullable=False)


