from fastapi import FastAPI
from routers import usuarios
from database import engine, Base

app = FastAPI()

app.include_router(usuarios.router, prefix="/api")


@app.on_event("startup")
def crear_tablas():
    Base.metadata.create_all(bind=engine)