from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.jwt import obtener_usuario_actual
from models.usuarios import Usuario
from database import get_db
from crud.dashboard import obtener_totales_dashboard, obtener_personas_por_tiposangre, obtener_areas_por_sucursal  # importar tu función
from collections import defaultdict
from typing import List, Dict, Any

router = APIRouter()

@router.get("/totals")
def get_dashboard_totals(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    try:
        return obtener_totales_dashboard(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/personas-por-tiposangre/")
def get_personas_por_tiposangre(db: Session = Depends(get_db)):
    """
    Endpoint para obtener una lista de personas agrupadas por tipo de sangre desde la vista.
    
    Retorna:
    - Una lista de personas con su tipo de sangre.
    """
    try:
        return obtener_personas_por_tiposangre(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los datos: {str(e)}")

@router.get("/areas-por-sucursal/", response_model=Dict[str, Any])
async def get_areas_por_sucursal(db: Session = Depends(get_db)):
    return obtener_areas_por_sucursal(db)