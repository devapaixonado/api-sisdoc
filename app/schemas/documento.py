from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentoBase(BaseModel):
    id_documento: int = None
    id_pasta: int = None
    id_usuario_ultima_atualizacao: int = None
    nome: str
    descricao: Optional[str] = None
    conteudo: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    dt_ultima_atualizacao: Optional[datetime] = None

class DocumentoCreate(BaseModel):
    id_pasta: int
    id_usuario_ultima_atualizacao: int
    nome: str
    descricao: Optional[str] = None
    conteudo: Optional[str] = None
    
class DocumentoFiltro(BaseModel):
    id_documento: Optional[int] = None
    id_pasta: Optional[int] = None
    id_usuario_ultima_atualizacao: Optional[int] = None
    nome: Optional[str] = None
    descricao: Optional[str] = None
    conteudo: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    dt_ultima_atualizacao: Optional[datetime] = None

class DocumentoUpdate(BaseModel):
    id_pasta: Optional[int] = None
    id_usuario_ultima_atualizacao: Optional[int] = None
    nome: Optional[str] = None
    descricao: Optional[str] = None
    conteudo: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    dt_ultima_atualizacao: Optional[datetime] = None
    
class DocumentoBaseOut(DocumentoBase):
    id_documento: int

    class Config:
        orm_mode = True
