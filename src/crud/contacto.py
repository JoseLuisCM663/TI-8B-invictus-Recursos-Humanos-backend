from pymongo.collection import Collection
from schemas.contacto import ContactoBase
from bson import ObjectId
from datetime import datetime


def crear_contacto(contacto: ContactoBase, mongo_db) -> dict:
    coleccion: Collection = mongo_db["contactos"]
    result = coleccion.insert_one(contacto.dict())
    return {"id": str(result.inserted_id), **contacto.dict()}


def obtener_contactos(mongo_db) -> list:
    coleccion: Collection = mongo_db["contactos"]
    contactos = list(coleccion.find())
    for contacto in contactos:
        contacto["_id"] = str(contacto["_id"])
    return contactos

def obtener_contacto(contacto_id: str, mongo_db) -> dict:
    coleccion: Collection = mongo_db["contactos"]
    contacto = coleccion.find_one({"_id": ObjectId(contacto_id)})
    if contacto:
        contacto["_id"] = str(contacto["_id"])
        return contacto
    return None

def actualizar_contacto(contacto_id: str, contacto: ContactoBase, mongo_db) -> dict:
    coleccion: Collection = mongo_db["contactos"]
    
    # Convertimos los datos del modelo a diccionario y agregamos la fecha de actualización
    datos_actualizados = contacto.dict()
    datos_actualizados["fecha_actualizacion"] = datetime.utcnow()

    resultado = coleccion.update_one(
        {"_id": ObjectId(contacto_id)},
        {"$set": datos_actualizados}
    )

    if resultado.modified_count == 0:
        return {"mensaje": "No se actualizó nada"}
    
    return {"id": contacto_id, **datos_actualizados}

def eliminar_contacto(contacto_id: str, mongo_db) -> dict:
    coleccion: Collection = mongo_db["contactos"]
    resultado = coleccion.delete_one({"_id": ObjectId(contacto_id)})
    if resultado.deleted_count == 0:
        return {"mensaje": "No se eliminó nada"}
    return {"mensaje": "Contacto eliminado", "id": contacto_id}
