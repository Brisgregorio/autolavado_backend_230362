import models.auto_servicio as model_auto_servicio
from sqlalchemy.orm import Session

def get_auto_servicio(db: Session, skip: int = 0, limit: int = 100):
    '''Función para obtener los autos de servicio'''
    return db.query(model_auto_servicio.AutoServicio).offset(skip).limit(limit).all()

import models.model_usuario 
import schemas.schema_usuario
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from passlib.exc import UnknownHashError
import models, schemas

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_user(db: Session, skip: int = 0, limit: int = 100):
    '''Función para obtener los usuarios'''
    return db.query(models.model_usuario.User).offset(skip).limit(limit).all()

def get_user_by_nombre(db: Session, nombre: str):
    '''Función para obtener un usuario por su nombre'''
    return db.query(models.model_usuario.User).filter(models.model_usuario.User.nombre == nombre).first()

def get_user_by_email(db: Session, correo_electronico: str):
    '''Función para obtener un usuario por su correo electrónico'''
    return db.query(models.model_usuario.User).filter(models.model_usuario.User.correo_electronico == correo_electronico).first()

def create_user(db: Session, user: schemas.schema_usuario.UserCreate):
    '''Función para crear un nuevo usuario'''
    hashed_password = pwd_context.hash(user.contrasena)
    db_user = models.model_usuario.User(
        rol_id=user.Rol_id,
        nombre=user.nombre,
        primer_apellido=user.primer_apellido,
        segundo_apellido=user.segundo_apellido,
        direccion=user.direccion,
        correo_electronico=user.correo_electronico,
        numero_telefono=user.numero_telefono,
        contrasena=hashed_password,
        estatus=user.estatus,
        fecha_registro=user.fecha_registro,
        fecha_actualizacion=user.fecha_actualizacion
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.schema_usuario.UserUpdate):
    '''Función para actualizar un usuario existente'''
    db_user = db.query(models.model_usuario.User).filter(models.model_usuario.User.id == user_id).first()
    if db_user is None:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.add(db_user)
        db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    '''Función para eliminar un usuario'''
    db_user = db.query(models.model_usuario.User).filter(models.model_usuario.User.id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
    