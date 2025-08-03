from sqlalchemy import Column, Integer, String, DateTime, Text
from app.db.base import Base
from datetime import datetime, timezone

class Documento(Base):
    __tablename__ = "documento"
    __table_args__ = {"schema": "sisdoc"}

    id_documento = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_topico = Column(Integer, nullable=False)
    id_usuario = Column(Integer, nullable=False)
    nome_arquivo = Column(String(255), nullable=False)
    descricao = Column(Text)
    tipo_arquivo = Column(String(50))
    caminho_arquivo = Column(Text)
    dt_inicio_vigencia = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    dt_fim_vigencia = Column(DateTime(timezone=True))