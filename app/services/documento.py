from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.documento import Documento
from app.schemas.documento import (
    DocumentoFiltro, DocumentoCreate, DocumentoUpdate
)

def create_documento(db: Session, data: DocumentoCreate):
    documentoExists = db.query(Documento).filter(
        Documento.nome == data.nome
    ).first()

    if documentoExists:
        raise ValueError(f"O documento {data.nome} já existe!")

    documento = Documento(**data.dict())
    db.add(documento)
    db.commit()
    db.refresh(documento)
    return documento

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
    if filtros.id_pasta:
        query = query.filter(Documento.id_pasta == filtros.id_pasta)
    if filtros.id_usuario_ultima_atualizacao:
        query = query.filter(Documento.id_usuario_ultima_atualizacao == filtros.id_usuario_ultima_atualizacao)
    if filtros.nome:
        query = query.filter(Documento.nome.ilike(f"%{filtros.nome}%"))
    if filtros.descricao:
        query = query.filter(Documento.descricao.ilike(f"%{filtros.descricao}%"))
    if filtros.conteudo:
        query = query.filter(Documento.conteudo.ilike(f"%{filtros.conteudo}%"))
    if filtros.dt_inicio_vigencia:
        query = query.filter(Documento.dt_inicio_vigencia == filtros.dt_inicio_vigencia)
    if filtros.dt_fim_vigencia:
        query = query.filter(Documento.dt_fim_vigencia == filtros.dt_fim_vigencia)
    if filtros.dt_ultima_atualizacao:
        query = query.filter(Documento.dt_ultima_atualizacao == filtros.dt_ultima_atualizacao)

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