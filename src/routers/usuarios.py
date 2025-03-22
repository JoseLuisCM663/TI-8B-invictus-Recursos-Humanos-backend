# routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.usuarios import UsuarioCreate, UsuarioResponse, LoginRequest
from crud.usuarios import crear_usuario, autenticar_usuario, crear_token_acceso, ACCESS_TOKEN_EXPIRE_MINUTES
from database import get_db  # Asegúrate de importar get_db
from datetime import datetime,timedelta



router = APIRouter()

@router.post("/registro/", response_model=UsuarioResponse)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Llamar a la función de la capa CRUD
    db_usuario = crear_usuario(db, usuario)
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de usuario o correo electronico ya está registrado",
        )
    return db_usuario

@router.post("/login")
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    # Autenticar al usuario
    usuario = autenticar_usuario(db, login_request.Correo_Electronico, login_request.Contrasena)

    # Crear el token de acceso
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crear_token_acceso(
        data={"sub": usuario.Correo_Electronico},  # Puedes incluir más datos aquí
        expires_delta=access_token_expires,
    )

    # Devolver el token
    return {"access_token": access_token, "token_type": "bearer"}
