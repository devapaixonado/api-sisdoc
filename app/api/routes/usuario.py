from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.usuario import UsuarioBaseOut, UsuarioFiltro, UsuarioCreate, UsuarioUpdate
from app.services import usuario

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=UsuarioBaseOut, status_code=201)
def create_usuario(grupo_data: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario.create_usuario(db, grupo_data)

# 🔹 GET: listar todos os usuários
@router.get("/", response_model=list[UsuarioBaseOut])
def get_all_usuarios(db: Session = Depends(get_db)):
    return usuario.get_all_usuarios(db)

# 🔹 GET: buscar usuário por ID
@router.get("/{id_usuario}", response_model=UsuarioBaseOut)
def get_usuario(id_usuario: int, db: Session = Depends(get_db)):
    return usuario.get_usuario(db, id_usuario)

# 🔹 POST: buscar usuários por filtros
@router.post("/", response_model=list[UsuarioBaseOut])
def search_usuarios_by_filters(filtros: UsuarioFiltro, db: Session = Depends(get_db)):
    return usuario.search_usuarios_by_filters(db, filtros)

@router.put("/{id_usuario}", response_model=UsuarioBaseOut)
def update_usuario(
    id_usuario: str,
    usuario_data: UsuarioUpdate,
    db: Session = Depends(get_db)
):
    return usuario.update_usuario(
        db, id_usuario, usuario_data
    )
