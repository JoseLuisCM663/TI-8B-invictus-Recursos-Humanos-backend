from sqlalchemy.orm import Session
from datetime import datetime
from models.horarios import TbbHorarios  # Tu modelo SQLAlchemy
from schemas.horarios import TbbHorariosCreate

def create_horario(db: Session, horario: TbbHorariosCreate):
    # Crear una nueva instancia de TbbHorarios con los datos de Pydantic
    nuevo_horario = TbbHorarios(
        ID_Colaborador=horario.ID_Colaborador if horario.ID_Colaborador is not None else None,
        Tipo=horario.Tipo,
        Hora_Inicio=horario.Hora_Inicio,
        Hora_Fin=horario.Hora_Fin,
        Fecha_Registro=datetime.now(),  # Se establece automáticamente
        Fecha_Actualizacion=datetime.now(),  # Se establece automáticamente
        Estatus=horario.Estatus,  # Valor por defecto
        Id_Sucursal=horario.Id_Sucursal if horario.Id_Sucursal is not None else None,
        Id_Servicio=horario.Id_Servicio if horario.Id_Servicio is not None else None,
    )

    # Agregar la nueva instancia a la sesión de la base de datos
    db.add(nuevo_horario)
    db.commit()  # Confirmar la transacción
    db.refresh(nuevo_horario)  # Obtener los valores actualizados (como el ID generado automáticamente)

    return nuevo_horario

