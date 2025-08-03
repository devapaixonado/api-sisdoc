from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 🔸 Schema base para criação/edição
class UsuarioBase(BaseModel):
    nome: str
    email: str
    senha: Optional[str] = None 
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: Optional[str] = None
    
# 🔍 Schema para filtros em buscas
class UsuarioFiltro(BaseModel):
    id_usuario: Optional[int] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    
# 🔸 Schema de saída (com ID gerado e orm_mode habilitado)
class UsuarioBaseOut(UsuarioBase):
    id_usuario: int

    class Config:
        orm_mode = True
