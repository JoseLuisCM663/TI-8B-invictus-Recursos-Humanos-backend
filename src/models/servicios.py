from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime, ForeignKey
from database import Base
from datetime import datetime
import enum
from sqlalchemy.orm import relationship


# Definimos el Enum para Tipo_Servicio
class TipoServicio(enum.Enum):
    entrenamiento_cardiovascular = "entrenamiento_cardiovascular"
    entrenamiento_fuerza = "entrenamiento_fuerza"
    yoga = "yoga"
    pilates = "pilates"
    spa = "spa"
    masaje_relajante = "masaje_relajante"
    masaje_deportivo = "masaje_deportivo"
    terapia_fisica = "terapia_fisica"
    evaluacion_fisica = "evaluacion_fisica"
    plan_entrenamiento = "plan_entrenamiento"
    asesoramiento_nutricional = "asesoramiento_nutricional"
    entrenamiento_funcional = "entrenamiento_funcional"
    crossfit = "crossfit"
    spinning = "spinning"
    baile = "baile"
    otro = "otro"


# Modelo SQLAlchemy para la tabla tbb_servicios
class TbbServicios(Base):
    __tablename__ = "tbb_servicios"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Sucursal_ID = Column(Integer, ForeignKey('tbc_sucursales.ID'), nullable=False)  # Relación con Sucursales
    Horario_ID = Column(Integer, ForeignKey('tbb_horarios.ID'), nullable=True)  # Relación con Horarios
    Colaborador_ID = Column(Integer, ForeignKey('tbb_personas.ID'), nullable=False)  # Relación con Colaboradores
    Tipo_Servicio = Column(Enum(TipoServicio), nullable=False)
    Descripcion = Column(String(255), nullable=True)
    Comentarios = Column(String(200), nullable=True)
    Estatus = Column(Boolean, default=True)
    Fecha_Registro = Column(DateTime, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    sucursal = relationship('TbcSucursales', backref='servicios')
    horario = relationship('TbbHorarios', backref='servicios')
    colaborador = relationship('TbbPersonas', backref='servicios')