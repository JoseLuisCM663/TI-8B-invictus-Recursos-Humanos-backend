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
    Id_persona: Optional[int] = None  # Opcional
    descripcion: str  # Campo obligatorio
    tipo: TipoQueja  # Enum obligatorio
    respuesta: Optional[str] = None  # Opcional
    estatus: EstatusQueja  # Enum obligatorio

# Clase para crear una nueva queja o sugerencia
class QuejasSugerenciasCreate(QuejasSugerenciasBase):
    pass  # Hereda todo de la clase base

# Clase para actualizar una queja o sugerencia existente
class QuejasSugerenciasUpdate(QuejasSugerenciasBase):
    pass  # Hereda todo de la clase base

# Clase para la respuesta del modelo de QuejasSugerencias
class QuejasSugerenciasResponse(QuejasSugerenciasBase):
    id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True  # Habilita el modo ORM para trabajar con SQLAlchemy
