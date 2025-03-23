from sqlalchemy.orm import Session
from models.colaboradores import Colaborador
from schemas.colaborador import ColaboradorCreate, ColaboradorUpdate
from fastapi import HTTPException, status
from datetime import datetime

# funcion para crear un nuevo colaborador
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

#funcion para obtener todos los colaboradores
def All_colaboradores(db: Session):
    """
    Obtener todos los colaboradores de la base de datos.
    """
    return db.query(Colaborador).all()

#funcion para actualizar un colaborador
def update_colaborador(db: Session, colaborador_id: int, colaborador_data: ColaboradorUpdate):
    """
    Actualizar un colaborador existente.
    """
    colaborador = db.query(Colaborador).filter(Colaborador.ID == colaborador_id).first()
    if not colaborador:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Colaborador no encontrado")

    for key, value in colaborador_data.dict(exclude_unset=True).items():
        setattr(colaborador, key, value)

    colaborador.Fecha_Actualizacion = datetime.now()  # Actualizar la fecha de modificación
    db.commit()
    db.refresh(colaborador)
    return colaborador

#funcion para eliminar un colaborador
def delete_colaborador(db: Session, colaborador_id: int):
    """
    Eliminar un colaborador por su ID.
    """
    colaborador = db.query(Colaborador).filter(Colaborador.ID == colaborador_id).first()
    if not colaborador:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Colaborador no encontrado")

    db.delete(colaborador)
    db.commit()
    return colaborador