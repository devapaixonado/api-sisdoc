from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TopicoBase(BaseModel):
    id_topico: int = None
    id_secao: int = None
    id_usuario: int = None
    descricao: str
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None

class TopicoCreate(BaseModel):
    id_secao: int
    id_usuario: int
    descricao: str
    
class TopicoFiltro(BaseModel):
    id_topico: Optional[int] = None
    id_secao: Optional[int] = None
    id_usuario: Optional[int] = None
    descricao: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None

class TopicoUpdate(BaseModel):
    id_secao: Optional[int] = None
    id_usuario: Optional[int] = None
    descricao: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    
class TopicoBaseOut(TopicoBase):
    id_topico: int

    class Config:
        orm_mode = True
