from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.secao import (
    SecaoBaseOut,
    SecaoFiltro,
    SecaoCreate,
    SecaoUpdate
)
from app.services import secao

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=SecaoBaseOut, status_code=201)
def create_secao(secao_data: SecaoCreate, db: Session = Depends(get_db)):
    return secao.create_secao(db, secao_data)

@router.get("/", response_model=list[SecaoBaseOut])
def get_all_secoes(db: Session = Depends(get_db)):
    return secao.get_all_secoes(db)

@router.get("/{id_secao}", response_model=SecaoBaseOut)
def get_secao(id_secao: int, db: Session = Depends(get_db)):
    return secao.get_secao(db, id_secao)

@router.post("/", response_model=list[SecaoBaseOut])
def search_secoes_by_filters(filtros: SecaoFiltro, db: Session = Depends(get_db)):
    return secao.search_secoes_by_filters(db, filtros)

@router.put("/{id_secao}", response_model=SecaoBaseOut)
def update_secao(
    id_secao: str,
    secao_data: SecaoUpdate,
    db: Session = Depends(get_db)
):
    return secao.update_secao(
        db, id_secao, secao_data
    )
