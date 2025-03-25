from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

from enum import Enum

# Definimos el Enum para Tipo_Servicio
class TipoServicio(str, Enum):
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


# Modelo base
class ServicioBase(BaseModel):
    Sucursal_ID: int
    Horario_ID: int
    Colaborador_ID: int
    Tipo_Servicio: TipoServicio
    Descripcion: Optional[str] = None
    Comentarios: Optional[str] = None
    Estatus: Optional[bool] = True  # Por defecto activo (1)

# Modelo para crear un servicio
class ServicioCreate(ServicioBase):
    pass  # No requiere atributos adicionales

# Modelo de respuesta para un servicio
class ServicioResponse(ServicioBase):
    ID: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

    class Config:
        orm_mode = True
