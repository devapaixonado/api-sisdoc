from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.base import Base
from datetime import datetime, timezone

class Pasta(Base):
    __tablename__ = "pasta"
    __table_args__ = {"schema": "sisdoc"}

    id_pasta = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario_ultima_atualizacao = Column(Integer, nullable=False)
    nome = Column(String(60), nullable=False)
    descricao = Column(String(255), nullable=True)
    dt_inicio_vigencia = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    dt_fim_vigencia = Column(DateTime(timezone=True))
    dt_ultima_atualizacao = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=func.now()
    )