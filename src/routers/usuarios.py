# routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.usuarios import UsuarioCreate, UsuarioResponse
from crud.usuarios import crear_usuario
from database import get_db  # Asegúrate de importar get_db
from datetime import datetime


router = APIRouter()

@router.post("/registro/", response_model=UsuarioResponse)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Llamar a la función de la capa CRUD
    db_usuario = crear_usuario(db, usuario)
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado",
        )
    return db_usuario
