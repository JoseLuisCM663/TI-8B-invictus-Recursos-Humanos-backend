from sqlalchemy.orm import Session
from models.usuarios import Usuario
from schemas.usuarios import UsuarioCreate
from passlib.context import CryptContext
from datetime import datetime
from fastapi import HTTPException, status


# Configuración para el hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para hashear la contraseña
def hash_contrasena(contrasena: str):
    return pwd_context.hash(contrasena)

# Función para crear un nuevo usuario
def crear_usuario(db: Session, usuario: UsuarioCreate):
    # Verificar si el correo ya está registrado
    db_usuario = db.query(Usuario).filter(
        (Usuario.Correo_Electronico == usuario.Correo_Electronico) | 
        (Usuario.Nombre_Usuario == usuario.Nombre_Usuario)
    ).first()
    if db_usuario:
        return None  # El correo o el nombre de usuario ya están registrados

    # Validar que la contraseña tenga al menos 8 caracteres
    if len(usuario.Contrasena) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña debe tener al menos 8 caracteres",
        )
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

# Función para verificar la contraseña
def verificar_contrasena(contrasena_plana: str, contrasena_hasheada: str):
    return pwd_context.verify(contrasena_plana, contrasena_hasheada)

# Función para autenticar al usuario
def autenticar_usuario(db: Session, username: str, password: str):
    # Buscar al usuario por correo electrónico
    usuario = db.query(Usuario).filter(Usuario.Correo_Electronico == username).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo electrónico o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Verificar la contraseña
    if not verificar_contrasena(password, usuario.Contrasena):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo electrónico o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return usuario