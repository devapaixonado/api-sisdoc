from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioFiltro
from app.schemas.usuario import UsuarioCreate
from app.schemas.usuario import UsuarioUpdate

def create_usuario(db: Session, data: UsuarioCreate):
    usuarioExists = db.query(Usuario).filter(
        Usuario.email == data.email
    ).first()

    if usuarioExists:
        raise ValueError(f"O email {data.email} já existe!")

    usuario = Usuario(**data.dict())
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def get_all_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario(db: Session, id_usuario: int):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

def search_usuarios_by_filters(db: Session, filtros: UsuarioFiltro):
    query = db.query(Usuario)

    if filtros.id_usuario:
        query = query.filter(Usuario.id_usuario == filtros.id_usuario)
    if filtros.nome:
        query = query.filter(Usuario.nome.ilike(f"%{filtros.nome}%"))
    if filtros.email:
        query = query.filter(Usuario.email.ilike(f"%{filtros.email}%"))
    if filtros.dt_inicio_vigencia:
        query = query.filter(Usuario.dt_inicio_vigencia == filtros.dt_inicio_vigencia)
    if filtros.dt_fim_vigencia:
        query = query.filter(Usuario.dt_fim_vigencia == filtros.dt_fim_vigencia)

    return query.all()

def update_usuario(db: Session, id_: str, data: UsuarioUpdate):
    usuario = db.query(Usuario).filter(
        Usuario.id_usuario == id_
    ).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(usuario, field, value)

    db.commit()
    db.refresh(usuario)
    return usuario