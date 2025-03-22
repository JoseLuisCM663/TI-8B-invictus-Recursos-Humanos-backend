from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey
from database import Base

class Usuario(Base):
    __tablename__ = "tbb_usuarios"
    
    ID = Column(Integer, primary_key=True, autoincrement=True, index=True)
    Nombre_Usuario = Column(String(50), unique=True, index=True)
    Persona_Id = Column(Integer, nullable=True)  # Elimina ForeignKey temporalmente 
    Correo_Electronico = Column(String(100), unique=True, index=True)
    Contrasena = Column(String(255))
    Numero_Telefonico_Movil = Column(String(20))
    Estatus = Column(Enum('Activo', 'Inactivo', 'Bloqueado', 'Suspendido'), default='Activo')
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
