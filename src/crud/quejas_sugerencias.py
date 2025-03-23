from models.quejas_sugerencias import QuejasSugerencias
from sqlalchemy.orm import Session
from datetime import datetime
from schemas.quejas_sugerencias import QuejasSugerenciasUpdate
from fastapi import HTTPException


def All_quejas_sugerencias(db: Session):
    """
    Obtener todas las quejas y sugerencias de la base de datos.
    """
    return db.query(QuejasSugerencias).all()

def get_queja_sugerencia_by_id(db: Session, queja_sugerencia_id: int):
    """
    Obtener una queja o sugerencia por su ID.
    """
    queja_sugerencia = db.query(QuejasSugerencias).filter(QuejasSugerencias.ID == queja_sugerencia_id).first()
    if not queja_sugerencia:
        raise HTTPException(status_code=404, detail="Queja o sugerencia no encontrada")
    
    return db.query(QuejasSugerencias).filter(QuejasSugerencias.ID == queja_sugerencia_id).first()

def update_queja_sugerencia(db: Session, queja_sugerencia_id: int, queja_sugerencia_data: QuejasSugerenciasUpdate):
    """
    Actualizar una queja o sugerencia existente.
    """
    queja_sugerencia = db.query(QuejasSugerencias).filter(QuejasSugerencias.ID == queja_sugerencia_id).first()
    if not queja_sugerencia:
        return HTTPException(status_code=404, detail="Queja o sugerencia no encontrada")

    for key, value in queja_sugerencia_data.dict(exclude_unset=True).items():
        setattr(queja_sugerencia, key, value)

    queja_sugerencia.Fecha_Actualizacion = datetime.now()  # Actualizar la fecha de modificación
    db.commit()
    db.refresh(queja_sugerencia)
    return queja_sugerencia