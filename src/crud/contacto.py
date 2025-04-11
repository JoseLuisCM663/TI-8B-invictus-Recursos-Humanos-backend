from pymongo.collection import Collection
from schemas.contacto import ContactoBase

def crear_contacto(contacto: ContactoBase, mongo_db) -> dict:
    coleccion: Collection = mongo_db["contactos"]
    result = coleccion.insert_one(contacto.dict())
    return {"id": str(result.inserted_id), **contacto.dict()}
