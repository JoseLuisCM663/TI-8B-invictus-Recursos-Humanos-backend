from sqlalchemy.orm import Session
from models.colaboradores import Colaborador
from models.areas import Areas
from models.quejas_sugerencias import QuejasSugerencias
from fastapi import HTTPException
from database import get_db
from sqlalchemy import text


# Función para obtener los totales para el dashboard
def obtener_totales_dashboard(db: Session):
    total_colaboradores = db.query(Colaborador).count()
    total_areas = db.query(Areas).count()
    total_quejas = db.query(QuejasSugerencias).count()

    return {
        "total_colaboradores": total_colaboradores,
        "total_areas": total_areas,
        "total_quejas": total_quejas
    }

def obtener_personas_por_tiposangre(db: Session):
    try:
        # Ejecutar la consulta
        result = db.execute(text("SELECT * FROM gym_system.vw_personas_por_tiposangre"))
        
        # Convertir los resultados en una lista de diccionarios
        # Obtener las claves de las columnas
        columns = result.keys()
        
        # Convertir cada fila en un diccionario utilizando las claves de las columnas
        resultados = [dict(zip(columns, row)) for row in result.fetchall()]
        
        return resultados

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los datos: {str(e)}")
