from sqlalchemy.orm import Session
from models.colaboradores import Colaborador
from models.areas import Areas
from models.quejas_sugerencias import QuejasSugerencias

def obtener_totales_dashboard(db: Session):
    total_colaboradores = db.query(Colaborador).count()
    total_areas = db.query(Areas).count()
    total_quejas = db.query(QuejasSugerencias).count()

    return {
        "total_colaboradores": total_colaboradores,
        "total_areas": total_areas,
        "total_quejas": total_quejas
    }
