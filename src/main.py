from fastapi import FastAPI
from routers import usuarios
from routers import horarios
from routers import colaborador
from routers import quejas_sugerencias
from routers import areas
from routers import dashboard
from routers import contacto  # 👈 NUEVO IMPORT

from database import engine, Base
from models.quejas_sugerencias import QuejasSugerencias
from models.sucursales import TbcSucursales
from models.personas import TbbPersonas
from models.usuarios_roles import UserRoles
from models.roles import Roles
from models.areas import Areas

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # permite solo ese origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers existentes
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(horarios.router, prefix="/api/horarios", tags=["Horarios"])
app.include_router(colaborador.router, prefix="/api/colaboradores", tags=["Colaboradores"])
app.include_router(quejas_sugerencias.router, prefix="/api/quejas_sugerencias", tags=["Quejas y Sugerencias"])
app.include_router(areas.router, prefix="/api/areas", tags=["Areas"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(contacto.router, prefix="/api/contacto", tags=["Contacto"])  # 👈 NUEVA RUTA

# Crear las tablas automáticamente al arrancar la aplicación
@app.on_event("startup")
def crear_tablas():
    Base.metadata.create_all(bind=engine)
