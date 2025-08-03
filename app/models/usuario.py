from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime, timezone

class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = {"schema": "sisdoc"}

    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(60))
    dt_inicio_vigencia = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    dt_fim_vigencia = Column(DateTime(timezone=True))