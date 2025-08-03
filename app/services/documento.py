from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.documento import Documento
from app.schemas.documento import (
    DocumentoFiltro, DocumentoCreate, DocumentoUpdate
)

def create_documento(db: Session, data: DocumentoCreate):
    secaoExists = db.query(Documento).filter(
        Documento.descricao == data.descricao
    ).first()

    if secaoExists:
        raise ValueError(f"O documento {data.descricao} já existe!")

    secao = Documento(**data.dict())
    db.add(secao)
    db.commit()
    db.refresh(secao)
    return secao

def get_all_documentos(db: Session):
    return db.query(Documento).all()

def get_documento(db: Session, id_documento: int):
    documento = db.query(Documento).filter(Documento.id_documento == id_documento).first()
    if not documento:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    return documento

def search_documentos_by_filters(db: Session, filtros: DocumentoFiltro):
    query = db.query(Documento)

    if filtros.id_documento:
        query = query.filter(Documento.id_documento == filtros.id_documento)
    if filtros.id_topico:
        query = query.filter(Documento.id_topico == filtros.id_topico)
    if filtros.id_usuario:
        query = query.filter(Documento.id_usuario == filtros.id_usuario)
    if filtros.nome_arquivo:
        query = query.filter(Documento.nome_arquivo.ilike(f"%{filtros.nome_arquivo}%"))
    if filtros.descricao:
        query = query.filter(Documento.descricao.ilike(f"%{filtros.descricao}%"))
    if filtros.descricao:
        query = query.filter(Documento.tipo_arquivo.ilike(f"%{filtros.tipo_arquivo}%"))
    if filtros.caminho_arquivo:
        query = query.filter(Documento.caminho_arquivo.ilike(f"%{filtros.caminho_arquivo}%"))
    if filtros.dt_inicio_vigencia:
        query = query.filter(Documento.dt_inicio_vigencia == filtros.dt_inicio_vigencia)
    if filtros.dt_fim_vigencia:
        query = query.filter(Documento.dt_fim_vigencia == filtros.dt_fim_vigencia)

    return query.all()

def update_documento(db: Session, id_: str, data: DocumentoUpdate):
    documento = db.query(Documento).filter(
        Documento.id_documento == id_
    ).first()

    if not documento:
        raise HTTPException(status_code=404, detail="Documento não encontrado")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(documento, field, value)

    db.commit()
    db.refresh(documento)
    return documento