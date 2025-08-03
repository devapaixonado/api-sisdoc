from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.topico import (
    TopicoBaseOut,
    TopicoFiltro,
    TopicoCreate,
    TopicoUpdate
)
from app.services import topico

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=TopicoBaseOut, status_code=201)
def create_topico(secao_data: TopicoCreate, db: Session = Depends(get_db)):
    return topico.create_topico(db, secao_data)

@router.get("/", response_model=list[TopicoBaseOut])
def get_all_topicos(db: Session = Depends(get_db)):
    return topico.get_all_topicos(db)

@router.get("/{id_topico}", response_model=TopicoBaseOut)
def get_topico(id_topico: int, db: Session = Depends(get_db)):
    return topico.get_topico(db, id_topico)

@router.post("/", response_model=list[TopicoBaseOut])
def search_topicos_by_filters(filtros: TopicoFiltro, db: Session = Depends(get_db)):
    return topico.search_topicos_by_filters(db, filtros)

@router.put("/{id_secao}", response_model=TopicoBaseOut)
def update_topico(
    id_secao: str,
    secao_data: TopicoUpdate,
    db: Session = Depends(get_db)
):
    return topico.update_topico(
        db, id_secao, secao_data
    )
