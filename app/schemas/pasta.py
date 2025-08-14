from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PastaBase(BaseModel):
    id_pasta: int = None
    id_usuario_ultima_atualizacao: int = None
    nome: str
    descricao: str
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    dt_ultima_atualizacao: Optional[datetime] = None

class PastaCreate(BaseModel):
    id_pasta: int
    id_usuario_ultima_atualizacao: int
    nome: str
    descricao: str
    
class PastaFiltro(BaseModel):
    id_topico: Optional[int] = None
    id_usuario_ultima_atualizacao: Optional[int] = None
    nome: Optional[str] = None
    descricao: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    dt_ultima_atualizacao: Optional[datetime] = None

class PastaUpdate(BaseModel):
    id_usuario_ultima_atualizacao: Optional[int] = None
    descricao: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    dt_ultima_atualizacao: Optional[datetime] = None
    
class PastaBaseOut(PastaBase):
    id_pasta: int

    class Config:
        orm_mode = True
