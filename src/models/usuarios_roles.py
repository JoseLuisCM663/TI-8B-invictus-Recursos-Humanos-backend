from sqlalchemy import Column, Integer, String, DateTime,Text,Boolean,ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class UserRoles(Base):
    __tablename__ = "tbd_usuarios_roles"    

    ID = Column(Integer,primary_key=True,autoincrement=True,index=True)
    Usuario_ID = Column(Integer, ForeignKey('tbb_usuarios.ID'), nullable=False)
    Rol_ID = Column(Integer, ForeignKey('tbc_roles.ID'), nullable=False)
    Estatus = Column(Boolean, default=True)
    Fecha_Registro = Column(DateTime, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


