from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

# Definición de los enums para Pydantic
class TipoQueja(str, Enum):
    sugerencia = "sugerencia"
    queja = "queja"
    reclamo = "reclamo"

class EstatusQueja(str, Enum):
    respondida = "respondida"
    espera = "espera"
    archivada = "archivada"

# Clase base para el modelo de QuejasSugerencias
class QuejasSugerenciasBase(BaseModel):
    Persona_ID: Optional[int] = None  # Opcional
    Descripcion: str  # Campo obligatorio
    Tipo: TipoQueja  # Enum obligatorio
    Respuesta: Optional[str] = None  # Opcional
    Estatus: EstatusQueja  # Enum obligatorio

# Clase para crear una nueva queja o sugerencia
class QuejasSugerenciasCreate(QuejasSugerenciasBase):
    pass  # Hereda todo de la clase base

# Clase para actualizar una queja o sugerencia existente
class QuejasSugerenciasUpdate(QuejasSugerenciasBase):
    pass  # Hereda todo de la clase base

# Clase para la respuesta del modelo de QuejasSugerencias
class QuejasSugerenciasResponse(QuejasSugerenciasBase):
    ID: int
    Fecha_registro: datetime
    Fecha_actualizacion: datetime

    class Config:
        orm_mode = True  # Habilita el modo ORM para trabajar con SQLAlchemy
