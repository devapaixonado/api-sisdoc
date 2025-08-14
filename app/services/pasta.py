from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.pasta import Pasta
from app.schemas.pasta import (
    PastaFiltro, PastaCreate, PastaUpdate
)

def create_pasta(db: Session, data: PastaCreate):
    pastaExists = db.query(Pasta).filter(
        Pasta.descricao == data.descricao
    ).first()

    if pastaExists:
        raise ValueError(f"A pasta {data.descricao} já existe!")

    pasta = Pasta(**data.dict())
    db.add(pasta)
    db.commit()
    db.refresh(pasta)
    return pasta

def get_all_pastas(db: Session):
    return db.query(Pasta).all()

def get_pasta(db: Session, id_pasta: int):
    pasta = db.query(Pasta).filter(Pasta.id_pasta == id_pasta).first()
    if not pasta:
        raise HTTPException(status_code=404, detail="Pasta não encontrado")
    return pasta

def search_pastas_by_filters(db: Session, filtros: PastaFiltro):
    query = db.query(Pasta)

    if filtros.id_pasta:
        query = query.filter(Pasta.id_pasta == filtros.id_pasta)
    if filtros.id_usuario_ultima_atualizacao:
        query = query.filter(Pasta.id_usuario_ultima_atualizacao == filtros.id_usuario_ultima_atualizacao)
    if filtros.nome:
        query = query.filter(Pasta.nome.ilike(f"%{filtros.nome}%"))
    if filtros.descricao:
        query = query.filter(Pasta.descricao.ilike(f"%{filtros.descricao}%"))
    if filtros.dt_inicio_vigencia:
        query = query.filter(Pasta.dt_inicio_vigencia == filtros.dt_inicio_vigencia)
    if filtros.dt_fim_vigencia:
        query = query.filter(Pasta.dt_fim_vigencia == filtros.dt_fim_vigencia)

    return query.all()

def update_pasta(db: Session, id_: str, data: PastaUpdate):
    pasta = db.query(Pasta).filter(
        Pasta.id_pasta == id_
    ).first()

    if not pasta:
        raise HTTPException(status_code=404, detail="Pasta não encontrada")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(pasta, field, value)

    db.commit()
    db.refresh(pasta)
    return pasta