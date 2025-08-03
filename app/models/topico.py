from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime, timezone

class Topico(Base):
    __tablename__ = "topico"
    __table_args__ = {"schema": "sisdoc"}

    id_topico = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_secao = Column(Integer, nullable=False)
    id_usuario = Column(Integer, nullable=False)
    descricao = Column(String(40), nullable=False)
    dt_inicio_vigencia = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    dt_fim_vigencia = Column(DateTime(timezone=True))