from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.pasta import (
    PastaBaseOut,
    PastaFiltro,
    PastaCreate,
    PastaUpdate
)
from app.services import pasta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=PastaBaseOut, status_code=201)
def create_pasta(pasta_data: PastaCreate, db: Session = Depends(get_db)):
    return pasta.create_pasta(db, pasta_data)

@router.get("/", response_model=list[PastaBaseOut])
def get_all_pastas(db: Session = Depends(get_db)):
    return pasta.get_all_pastas(db)

@router.get("/{id_pasta}", response_model=PastaBaseOut)
def get_pasta(id_pasta: int, db: Session = Depends(get_db)):
    return pasta.get_pasta(db, id_pasta)

@router.post("/", response_model=list[PastaBaseOut])
def search_pastas_by_filters(filtros: PastaFiltro, db: Session = Depends(get_db)):
    return pasta.search_pastas_by_filters(db, filtros)

@router.put("/{id_pasta}", response_model=PastaBaseOut)
def update_pasta(
    id_pasta: str,
    pasta_data: PastaUpdate,
    db: Session = Depends(get_db)
):
    return pasta.update_pasta(
        db, id_pasta, pasta_data
    )
