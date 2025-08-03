from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.secao import Secao
from app.schemas.secao import (
    SecaoFiltro, SecaoCreate, SecaoUpdate
)


def create_secao(db: Session, data: SecaoCreate):
    secaoExists = db.query(Secao).filter(
        Secao.descricao == data.descricao
    ).first()

    if secaoExists:
        raise ValueError(f"A seção {data.descricao} já existe!")

    secao = Secao(**data.dict())
    db.add(secao)
    db.commit()
    db.refresh(secao)
    return secao

def get_all_secoes(db: Session):
    return db.query(Secao).all()

def get_secao(db: Session, id_secao: int):
    return db.query(Secao).filter(Secao.id_secao == id_secao).first()

def search_secoes_by_filters(db: Session, filtros: SecaoFiltro):
    query = db.query(Secao)

    if filtros.id_secao:
        query = query.filter(Secao.id_secao == filtros.id_secao)
    if filtros.id_usuario:
        query = query.filter(Secao.id_usuario == filtros.id_usuario)
    if filtros.descricao:
        query = query.filter(Secao.descricao.ilike(f"%{filtros.descricao}%"))
    if filtros.dt_inicio_vigencia:
        query = query.filter(Secao.dt_inicio_vigencia == filtros.dt_inicio_vigencia)
    if filtros.dt_fim_vigencia:
        query = query.filter(Secao.dt_fim_vigencia == filtros.dt_fim_vigencia)

    return query.all()

def update_secao(db: Session, id_: str, data: SecaoUpdate):
    secao = db.query(Secao).filter(
        Secao.id_secao == id_
    ).first()

    if not secao:
        raise HTTPException(status_code=404, detail="Seção não encontrado")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(secao, field, value)

    db.commit()
    db.refresh(secao)
    return secao