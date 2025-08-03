from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 🔸 Schema base para criação/edição
class SecaoBase(BaseModel):
    id_secao: int = None
    id_usuario: int = None
    descricao: str
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None

class SecaoCreate(BaseModel):
    id_usuario: int
    descricao: str
    
# 🔍 Schema para filtros em buscas
class SecaoFiltro(BaseModel):
    id_secao: Optional[int] = None
    id_usuario: Optional[int] = None
    descricao: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None

class SecaoUpdate(BaseModel):
    id_usuario: Optional[int] = None
    descricao: Optional[str] = None
    dt_inicio_vigencia: Optional[datetime] = None
    dt_fim_vigencia: Optional[datetime] = None
    
# 🔸 Schema de saída (com ID gerado e orm_mode habilitado)
class SecaoBaseOut(SecaoBase):
    id_secao: int

    class Config:
        orm_mode = True
