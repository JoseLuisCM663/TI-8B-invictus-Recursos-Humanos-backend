from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.servicios import ServicioCreate
from models.usuarios import Usuario  # Tu modelo para usuarios
from models.servicios import TbbServicios  # Tu modelo SQLAlchemy
from crud.servicios import  All_servicios, update_servicio,servicio_by_id  # La función que creaste para insertar horarios
from config.jwt import obtener_usuario_actual  # Dependencia que verifica al usuario autenticado
from database import get_db

router = APIRouter()

# Ruta protegida que requiere autenticación para obtener todos los servicios
@router.get("/servicios/")
def obtener_servicios(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)  # Verifica que el usuario esté autenticado
):
    """
    Endpoint protegido para obtener todos los servicios de la base de datos.
    Requiere autenticación.
    """
    try:
        return All_servicios(db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Ruta protegida que requiere autenticación para actualizar un servicio
@router.put("/servicios/{servicio_id}", response_model=ServicioCreate)
def actualizar_servicio(
    servicio_id: int,
    servicio_data: ServicioCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)  # Verifica que el usuario esté autenticado
):
    """
    Endpoint protegido para actualizar un servicio existente.
    Requiere autenticación.
    """
    try:
        return update_servicio(db=db, servicio_id=servicio_id, servicio_data=servicio_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

#Ruta protegida que requiere autenticación para obtener un servicio por su ID
@router.get("/servicios/{servicio_id}", response_model=ServicioCreate)
def obtener_servicio_por_id(
    servicio_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)  # Verifica que el usuario esté autenticado
):
    """
    Endpoint protegido para obtener un servicio por su ID.
    Requiere autenticación.
    """
    try:
        servicio = servicio_by_id(db=db, servicio_id=servicio_id)
        if not servicio:
            raise HTTPException(status_code=404, detail="Servicio no encontrado")
        return servicio
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))