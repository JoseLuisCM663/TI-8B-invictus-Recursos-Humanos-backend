from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.horarios import TbbHorariosCreate
from models.usuarios import Usuario  # Tu modelo para usuarios
from crud.horarios import create_horario  # La función que creaste para insertar horarios
from config.jwt import obtener_usuario_actual  # Dependencia que verifica al usuario autenticado
from database import get_db

router = APIRouter()

# Ruta protegida que requiere autenticación
@router.post("/horarios/", response_model=TbbHorariosCreate)
def crear_horario(
    horario: TbbHorariosCreate, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)  # Verifica que el usuario esté autenticado
):
    """
    Endpoint para crear un nuevo horario en la base de datos.
    Requiere autenticación.
    """
    if not usuario or not usuario.is_active:
        raise HTTPException(
            status_code=403, detail="No tienes permiso para realizar esta acción"
        )

    # Crear un nuevo horario usando la función que hemos definido
    try:
        return create_horario(db=db, horario=horario)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
