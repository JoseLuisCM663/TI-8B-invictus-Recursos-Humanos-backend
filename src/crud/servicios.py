from sqlalchemy.orm import Session
from datetime import datetime
from models.servicios import TbbServicios  # Tu modelo SQLAlchemy
from schemas.servicios import ServicioCreate

def update_servicio(db: Session, servicio_id: int, servicio_data: ServicioCreate):
    """
    Actualizar un servicio existente.
    """
    servicio = db.query(TbbServicios).filter(TbbServicios.ID == servicio_id).first()
    if not servicio:
        return None

    for key, value in servicio_data.dict(exclude_unset=True).items():
        setattr(servicio, key, value)

    servicio.Fecha_Actualizacion = datetime.now()  # Actualizar la fecha de modificación
    db.commit()
    db.refresh(servicio)
    return servicio

def All_servicios(db: Session):
    """
    Obtener todos los servicios de la base de datos.
    """
    return db.query(TbbServicios).all()

def servicio_by_id(db: Session, servicio_id: int):
    """
    Obtener un servicio por su ID.
    """
    return db.query(TbbServicios).filter(TbbServicios.ID == servicio_id).first()