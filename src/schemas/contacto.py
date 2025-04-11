from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ContactoBase(BaseModel):
    nombre_completo: str
    correo: str
    celular: str
    comentario: Optional[str] = None
    fecha_registro: datetime = datetime.now()
    fecha_actualizacion: datetime = datetime.now()
