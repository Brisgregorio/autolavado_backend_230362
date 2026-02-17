import models.rol as model_rol
from sqlalchemy.orm import Session

def get_rol(db: Session, skip: int = 0, limit: int = 100):
    '''Función para obtener los roles'''
    return db.query(model_rol.Rol).offset(skip).limit(limit).all()

def get_roles(db: Session, skin: int = 0, limit: int = 100):
    return db.query(model_rol.Rol).offset(skip).limit(limit).all()

def create_rol(db: Session, rol: model_rol.RolCreate):
    '''Función para crear un nuevo rol'''
    db_rol = model_rol.Rol(nombre=rol.nombre)
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def update_rol(db: Session, rol_id: int, rol: model_rol.RolUpdate):
    '''Función para actualizar un rol existente'''
    db_rol = db.query(model_rol.Rol).filter(model_rol.Rol.id == rol_id).first()
    if db_rol is None:
        return None
    db_rol.nombre = rol.nombre
    db.commit()
    db.refresh(db_rol)
    return db_rol
def delete_rol(db: Session, rol_id: int):
    '''Función para eliminar un rol'''
    db_rol = db.query(model_rol.Rol).filter(model_rol.Rol.id == rol_id).first()
    if db_rol is None:
        return None
    db.delete(db_rol)
    db.commit()
    return db_rol