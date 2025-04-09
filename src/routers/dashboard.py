from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.jwt import obtener_usuario_actual
from models.usuarios import Usuario
from database import get_db
from crud.dashboard import obtener_totales_dashboard

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
