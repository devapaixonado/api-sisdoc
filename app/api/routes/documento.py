from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.documento import (
    DocumentoBaseOut,
    DocumentoFiltro,
    DocumentoCreate,
    DocumentoUpdate
)
from app.services import documento

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=DocumentoBaseOut, status_code=201)
def create_documento(secao_data: DocumentoCreate, db: Session = Depends(get_db)):
    return documento.create_documento(db, secao_data)

@router.get("/", response_model=list[DocumentoBaseOut])
def get_all_documentos(db: Session = Depends(get_db)):
    return documento.get_all_documentos(db)

@router.get("/{id_documento}", response_model=DocumentoBaseOut)
def get_documento(id_documento: int, db: Session = Depends(get_db)):
    return documento.get_documento(db, id_documento)


@router.post("/", response_model=list[DocumentoBaseOut])
def search_documentos_by_filters(filtros: DocumentoFiltro, db: Session = Depends(get_db)):
    return documento.search_documentos_by_filters(db, filtros)

@router.put("/{id_documento}", response_model=DocumentoBaseOut)
def update_documento(
    id_documento: str,
    documento_data: DocumentoUpdate,
    db: Session = Depends(get_db)
):
    return documento.update_documento(
        db, id_documento, documento_data
    )
