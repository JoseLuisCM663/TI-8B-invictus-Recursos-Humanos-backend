from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ColaboradorBase(BaseModel):
    Nombre: str
    Correo_Electronico: str
    Numero_Telefonico_Movil: Optional[str] = None
    Especialidad: Optional[str] = None
    Estatus: Optional[bool] = True  # 1 para 'activo', 0 para 'inactivo'
    
class ColaboradorCreate(ColaboradorBase):
    Persona_Id: Optional[int] = None
    Sucursal_Id: Optional[int] = None
    Servicio_Id: Optional[int] = None

class ColaboradorUpdate(ColaboradorBase):
    Persona_Id: Optional[int] = None
    Sucursal_Id: Optional[int] = None
    Servicio_Id: Optional[int] = None

class ColaboradorResponse(ColaboradorBase):
    ID: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

    class Config:
        orm_mode = True