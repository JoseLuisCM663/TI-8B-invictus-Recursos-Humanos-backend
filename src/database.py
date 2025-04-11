import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pymongo import MongoClient

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Construir la URL de conexión
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"charset": "utf8mb4"})

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Función para obtener una sesión de base de datos
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Conexión directa a MongoDB Atlas (sin .env)
MONGO_URI = "mongodb+srv://joseluis:1234@cluster0.1sonbs2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGO_DB = "db_gym"  # cámbialo por el nombre que quieras usar

# Crear cliente y base de datos
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB]

# Función para obtener la base de datos Mongo
def get_mongo_db():
    return mongo_db
