from sqlalchemy.orm import Session
from models.colaboradores import Colaborador
from models.areas import Areas
from models.quejas_sugerencias import QuejasSugerencias
from fastapi import HTTPException
from database import get_db
from sqlalchemy import text
from collections import defaultdict
from typing import List, Dict, Any


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


def obtener_areas_por_sucursal(db: Session) -> Dict[str, Any]:
    try:
        # Ejecutar la consulta
        result = db.execute(text("SELECT * FROM gym_system.vw_areas_por_sucursal ORDER BY Nombre_Sucursal"))
        
        # Convertir los resultados en una lista de diccionarios
        columns = result.keys()
        datos = [dict(zip(columns, row)) for row in result.fetchall()]
        
        # Procesar para agrupar por sucursal
        sucursales = defaultdict(list)
        for item in datos:
            sucursales[item['Sucursal_ID']].append({
                'Area_ID': item['Area_ID'],
                'Nombre_Area': item['Nombre_Area']
            })
        
        # Construir la respuesta estructurada
        respuesta = {
            'sucursales': [],
            'total_sucursales': len(sucursales),
            'total_areas': sum(len(areas) for areas in sucursales.values())
        }
        
        for sucursal_id, areas in sucursales.items():
            # Encontrar el nombre de la sucursal (tomamos el primero ya que es el mismo para todos)
            nombre_sucursal = next((item['Nombre_Sucursal'] for item in datos if item['Sucursal_ID'] == sucursal_id), None)
            
            respuesta['sucursales'].append({
                'id': sucursal_id,
                'nombre': nombre_sucursal,
                'total_areas': len(areas),
                'areas': areas
            })
        
        return respuesta

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener los datos: {str(e)}"
        )