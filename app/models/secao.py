from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime, timezone

class Secao(Base):
    __tablename__ = "secao"
    __table_args__ = {"schema": "sisdoc"}

    id_secao = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, nullable=False)
    descricao = Column(String(40), nullable=False)
    dt_inicio_vigencia = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    dt_fim_vigencia = Column(DateTime(timezone=True))