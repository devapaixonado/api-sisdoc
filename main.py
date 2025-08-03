from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import (
    usuario,
    secao
)

app = FastAPI(title="API SisDoc Postgres com SQLAlchemy")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # ou ["*"] no desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario.router, prefix="/api/usuarios", tags=["Usuario"])
app.include_router(secao.router, prefix="/api/secoes", tags=["Secao"])

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "🚀 API SisDoc is up and running!"}
