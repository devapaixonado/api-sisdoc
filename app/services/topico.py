from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.topico import Topico
from app.schemas.topico import (
    TopicoFiltro, TopicoCreate, TopicoUpdate
)

def create_topico(db: Session, data: TopicoCreate):
    topicoExists = db.query(Topico).filter(
        Topico.descricao == data.descricao
    ).first()

    if topicoExists:
        raise ValueError(f"O tópico {data.descricao} já existe!")

    topico = Topico(**data.dict())
    db.add(topico)
    db.commit()
    db.refresh(topico)
    return topico

def get_all_topicos(db: Session):
    return db.query(Topico).all()

def get_topico(db: Session, id_topico: int):
    topico = db.query(Topico).filter(Topico.id_topico == id_topico).first()
    if not topico:
        raise HTTPException(status_code=404, detail="Tópico não encontrado")
    return topico

def search_topicos_by_filters(db: Session, filtros: TopicoFiltro):
    query = db.query(Topico)

    if filtros.id_topico:
        query = query.filter(Topico.id_topico == filtros.id_topico)
    if filtros.id_secao:
        query = query.filter(Topico.id_secao == filtros.id_secao)
    if filtros.id_usuario:
        query = query.filter(Topico.id_usuario == filtros.id_usuario)
    if filtros.descricao:
        query = query.filter(Topico.descricao.ilike(f"%{filtros.descricao}%"))
    if filtros.dt_inicio_vigencia:
        query = query.filter(Topico.dt_inicio_vigencia == filtros.dt_inicio_vigencia)
    if filtros.dt_fim_vigencia:
        query = query.filter(Topico.dt_fim_vigencia == filtros.dt_fim_vigencia)

    return query.all()

def update_topico(db: Session, id_: str, data: TopicoUpdate):
    topico = db.query(Topico).filter(
        Topico.id_topico == id_
    ).first()

    if not topico:
        raise HTTPException(status_code=404, detail="Tópico não encontrado")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(topico, field, value)

    db.commit()
    db.refresh(topico)
    return topico