from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentoBase(BaseModel):
    id_documento: int = None
    id_topico: int = None
    id_usuario: int = None
    nome_arquivo: str
    descricao: Optional[str] = None
    tipo_arquivo: Optional[str] = None
    caminho_arquivo: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None

class DocumentoCreate(BaseModel):
    id_topico: int
    id_usuario: int
    nome_arquivo: str
    descricao: Optional[str] = None
    tipo_arquivo: Optional[str] = None
    caminho_arquivo: Optional[str] = None
    
class DocumentoFiltro(BaseModel):
    id_documento: Optional[int] = None
    id_topico: Optional[int] = None
    id_usuario: Optional[int] = None
    nome_arquivo: Optional[str] = None
    descricao: Optional[str] = None
    tipo_arquivo: Optional[str] = None
    caminho_arquivo: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None

class DocumentoUpdate(BaseModel):
    id_topico: Optional[int] = None
    id_usuario: Optional[int] = None
    nome_arquivo: Optional[str] = None
    descricao: Optional[str] = None
    tipo_arquivo: Optional[str] = None
    caminho_arquivo: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    
class DocumentoBaseOut(DocumentoBase):
    id_documento: int

    class Config:
        orm_mode = True
