# crud/usuarios.py
from sqlalchemy.orm import Session
from models.usuarios import Usuario
from schemas.usuarios import UsuarioCreate
from passlib.context import CryptContext
from datetime import datetime


# Configuración para el hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para hashear la contraseña
def hash_contrasena(contrasena: str):
    return pwd_context.hash(contrasena)

def crear_usuario(db: Session, usuario: UsuarioCreate):
    # Verificar si el correo ya está registrado
    db_usuario = db.query(Usuario).filter(Usuario.Correo_Electronico == usuario.Correo_Electronico).first()
    if db_usuario:
        return None  # El correo ya está registrado

    # Crear el nuevo usuario
    nuevo_usuario = Usuario(
        Persona_Id=usuario.Persona_Id if usuario.Persona_Id is not None else None,
        Nombre_Usuario=usuario.Nombre_Usuario,
        Correo_Electronico=usuario.Correo_Electronico,
        Contrasena=hash_contrasena(usuario.Contrasena),
        Numero_Telefonico_Movil=usuario.Numero_Telefonico_Movil,
        Estatus=usuario.Estatus,
        Fecha_Registro=datetime.now(),  # Establecer la fecha de registro actual
        Fecha_Actualizacion=datetime.now(),  # Establecer la fecha de actualización actual
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario