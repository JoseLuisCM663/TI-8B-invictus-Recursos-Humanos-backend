# routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.usuarios import Usuario
from schemas.usuarios import UsuarioCreate, UsuarioResponse, LoginRequest
from crud.usuarios import crear_usuario, autenticar_usuario,update_usuario,obtener_usuario_por_id
from database import get_db  # Asegúrate de importar get_db
from datetime import timedelta
from config.jwt import crear_token_acceso, obtener_usuario_actual, ACCESS_TOKEN_EXPIRE_MINUTES  # Importa desde config/jwt.py

router = APIRouter() 

@router.post("/registro/", response_model=UsuarioResponse)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Llamar a la función de la capa CRUD
    db_usuario = crear_usuario(db, usuario)
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de usuario o correo electronico ya está registrado",
        )
    return db_usuario

@router.post("/login")
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    # Autenticar al usuario
    usuario = autenticar_usuario(db, login_request.Correo_Electronico, login_request.Contrasena)

    # Crear el token de acceso
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crear_token_acceso(
        data={"sub": usuario.Correo_Electronico},  # Puedes incluir más datos aquí
        expires_delta=access_token_expires,
    )

    # Devolver el token
    return {"access_token": access_token, "token_type": "bearer"}

# Ruta protegida que requiere autenticación
@router.get("/usuario_protegido")
def obtener_usuario_protegido(usuario: Usuario = Depends(obtener_usuario_actual)):
    # Aquí el usuario ya está autenticado, puedes devolver información segura
    return {
        "message": "Acceso autorizado",
        "usuario": usuario.Correo_Electronico,
        "nombre_usuario": usuario.Nombre_Usuario,
    }

@router.put("/usuario/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(
    usuario_id: int,
    usuario_data: UsuarioCreate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)  # Verifica que el usuario esté autenticado
):
    """
    Endpoint protegido para actualizar un usuario existente.
    Requiere autenticación.
    """
    try:
        return update_usuario(db=db, usuario_id=usuario_id, usuario_data=usuario_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/usuario/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(
    usuario_id: int, 
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)  # Verifica que el usuario esté autenticado
    ):
    """
    Endpoint para obtener un usuario por su ID.
    """
    usuario = obtener_usuario_por_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario