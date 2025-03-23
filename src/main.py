from fastapi import FastAPI
from routers import usuarios
from routers import horarios
from routers import colaborador
from database import engine, Base

app = FastAPI()

# Asegúrate de que los prefijos sean diferentes si ambos routers contienen rutas diferentes.
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(horarios.router, prefix="/api/horarios", tags=["Horarios"])
app.include_router(colaborador.router, prefix="/api/colaboradores", tags=["Colaboradores"])
# Crear las tablas automáticamente al arrancar la aplicación
@app.on_event("startup")
def crear_tablas():
    # Crear todas las tablas definidas en los modelos
    Base.metadata.create_all(bind=engine)