from fastapi import APIRouter, Depends
from schemas.contacto import ContactoBase
from crud.contacto import crear_contacto,obtener_contacto,obtener_contactos,actualizar_contacto,eliminar_contacto
from database import get_mongo_db

router = APIRouter()

@router.post("/contacto")
def nuevo_contacto(contacto: ContactoBase, mongo_db = Depends(get_mongo_db)):
    return crear_contacto(contacto, mongo_db)

@router.get("/contacto")
def listar_contactos(mongo_db = Depends(get_mongo_db)):
    return obtener_contactos(mongo_db)

@router.get("/contacto/{contacto_id}")
def obtener_contacto1(contacto_id: str, mongo_db = Depends(get_mongo_db)):
    return obtener_contacto(contacto_id, mongo_db)

@router.put("/contacto/{contacto_id}")
def actualizar_contacto1(contacto_id: str, contacto: ContactoBase, mongo_db = Depends(get_mongo_db)):
    return actualizar_contacto(contacto_id, contacto, mongo_db)

@router.delete("/contacto/{contacto_id}")
def eliminar_contacto1(contacto_id: str, mongo_db = Depends(get_mongo_db)):
    return eliminar_contacto(contacto_id, mongo_db)
