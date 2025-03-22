from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    Nombre_Usuario: str
    Correo_Electronico: str
    Numero_Telefonico_Movil: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    Contrasena: str
    Persona_Id: Optional[int] = None  # Permite que Persona_Id sea null
    Estatus: Optional[str] = "Activo"  # Valor por defecto

class UsuarioResponse(UsuarioBase):
    ID: int
    Persona_Id: Optional[int] = None  
    Estatus: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

    class Config:
        orm_mode = True
    
class LoginRequest(BaseModel):
    Correo_Electronico: str
    Contrasena: str
