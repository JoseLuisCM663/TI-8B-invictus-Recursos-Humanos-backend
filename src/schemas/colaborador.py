from pydantic import BaseModel
from datetime import datetime
from typing import Optional

#clase base para el modelo de colaborador
class ColaboradorBase(BaseModel):
    Nombre: str
    Correo_Electronico: str
    Numero_Telefonico_Movil: Optional[str] = None
    Especialidad: Optional[str] = None
    Estatus: Optional[bool] = True  # 1 para 'activo', 0 para 'inactivo'
    
#clase para crear un nuevo colaborador
#hereda de la clase base ColaboradorBase
class ColaboradorCreate(ColaboradorBase):
    Persona_Id: Optional[int] = None
    Sucursal_Id: Optional[int] = None
    Servicio_Id: Optional[int] = None

#clase para actualizar un colaborador existente
class ColaboradorUpdate(ColaboradorBase):
    Persona_Id: Optional[int] = None
    Sucursal_Id: Optional[int] = None
    Servicio_Id: Optional[int] = None

#clase para la respuesta del colaborador
class ColaboradorResponse(ColaboradorBase):
    ID: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

    class Config:
        orm_mode = True