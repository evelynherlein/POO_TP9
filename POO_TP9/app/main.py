from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401  (registra las entidades en Base)
from app.database import Base, engine
from app.routers import acceso, cotizacion, pagos


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)  # crea las tablas en SQLite
    yield


app = FastAPI(
    title="SmartTicket API",
    description="Venta de entradas y control de acceso - TP 9 POO (GRASP y SOLID)",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(cotizacion.router)
app.include_router(pagos.router)
app.include_router(acceso.router)


@app.get("/", tags=["Health"])
def raiz():
    return {"status": "ok", "docs": "/docs"}
