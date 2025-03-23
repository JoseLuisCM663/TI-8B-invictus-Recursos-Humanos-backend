from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.colaboradores import Colaborador
from schemas.colaborador import ColaboradorCreate, ColaboradorResponse, ColaboradorUpdate
from crud.colaborador import crear_colaborador
from database import get_db  # Asegúrate de importar get_db
from datetime import timedelta
from config.jwt import obtener_usuario_actual, ACCESS_TOKEN_EXPIRE_MINUTES  # Importa desde config/jwt.py

router = APIRouter()

@router.post("/colaborador/", response_model=ColaboradorResponse)
def registrar_colaborador(colaborador: ColaboradorCreate, db: Session = Depends(get_db), usuario_actual: Colaborador = Depends(obtener_usuario_actual)):
    # Llamar a la función de la capa CRUD
    db_colaborador = crear_colaborador(db, colaborador)
    if not db_colaborador:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado",
        )
    return db_colaborador