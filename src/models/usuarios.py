from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "tbb_usuarios"
    
    ID = Column(Integer, primary_key=True, autoincrement=True, index=True)
    Nombre_Usuario = Column(String(50), unique=True, index=True)
    Persona_ID = Column(Integer, ForeignKey('tbb_personas.ID'), nullable=True)  # Relación con tbb_personas
    Correo_Electronico = Column(String(100), unique=True, index=True)
    Contrasena = Column(String(255))
    Numero_Telefonico_Movil = Column(String(20))
    Estatus = Column(Enum('Activo', 'Inactivo', 'Bloqueado', 'Suspendido'), default='Activo')
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    # Relación con TbbPersonas
    persona = relationship('TbbPersonas', backref='usuarios')