from sqlalchemy.orm import Session
from models.colaboradores import Colaborador
from schemas.colaborador import ColaboradorCreate, ColaboradorUpdate
from fastapi import HTTPException, status
from datetime import datetime


def crear_colaborador(db: Session, colaborador: ColaboradorCreate):
    # Verificar si el correo ya está registrado
    db_colaborador = db.query(Colaborador).filter(
        (Colaborador.Correo_Electronico == colaborador.Correo_Electronico)
    ).first()
    if db_colaborador:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado",
        )
    
    nuevo_colaborador = Colaborador(
        Nombre=colaborador.Nombre,
        Persona_Id=colaborador.Persona_Id if colaborador.Persona_Id is not None else None,
        Sucursal_Id=colaborador.Sucursal_Id if colaborador.Sucursal_Id is not None else None,
        Servicio_Id=colaborador.Servicio_Id if colaborador.Servicio_Id is not None else None,
        Correo_Electronico=colaborador.Correo_Electronico,
        Especialidad=colaborador.Especialidad,
        Numero_Telefonico_Movil=colaborador.Numero_Telefonico_Movil,
        Estatus=colaborador.Estatus,
        Fecha_Registro=datetime.now(),  # Establecer la fecha de registro actual
        Fecha_Actualizacion=datetime.now(),  # Establecer la fecha de actualización actual
    )
    db.add(nuevo_colaborador)
    db.commit()
    db.refresh(nuevo_colaborador)
    return nuevo_colaborador

