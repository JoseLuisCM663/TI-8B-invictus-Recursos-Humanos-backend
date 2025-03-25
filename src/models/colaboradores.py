from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#modelo para la tabla de colaboradores
#hereda de la clase Base de SQLAlchemy
class Colaborador(Base):
    __tablename__ = "tbb_colaboradores"
    
    ID = Column(Integer, primary_key=True, autoincrement=True, index=True)
    Nombre= Column(String(50))
    Persona_ID = Column(Integer, ForeignKey('tbb_personas.ID'), unique=True)  # Relación con TbbPersonas
    Horario_ID = Column(Integer, ForeignKey('tbb_horarios.ID'))  # Relación con TbbHorarios
    Correo_Electronico = Column(String(100), unique=True, index=True)
    Especialidad = Column(String(50), nullable=True)
    Numero_Telefonico_Movil = Column(String(20), nullable=True)
    Estatus = Column(Boolean, default=True)  # 1 para 'activo', 0 para 'inactivo'
    Fecha_Registro = Column(DateTime, nullable=False)
    Fecha_Actualizacion = Column(DateTime, nullable=False)

    # Relación con la tabla TbbPersonas (opcional)
    persona = relationship('TbbPersonas', backref='colaboradores')

    # Relación con la tabla TbbHorarios (opcional)
    horario = relationship('TbbHorarios', backref='colaboradores')