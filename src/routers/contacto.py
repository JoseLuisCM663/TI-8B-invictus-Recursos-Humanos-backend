from fastapi import APIRouter, Depends
from schemas.contacto import ContactoBase
from crud.contacto import crear_contacto
from database import get_mongo_db

router = APIRouter(prefix="/contacto", tags=["Contacto"])

@router.post("/")
def nuevo_contacto(contacto: ContactoBase, mongo_db = Depends(get_mongo_db)):
    return crear_contacto(contacto, mongo_db)