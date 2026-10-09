"""Entidades del dominio SmartTicket (solo atributos básicos, sin lógica)."""
import enum

from sqlalchemy import (
    Column, DateTime, Enum, Float, ForeignKey, Integer, String,
)
from sqlalchemy.orm import relationship

from app.database import Base


class EstadoEntrada(str, enum.Enum):
    DISPONIBLE = "DISPONIBLE"
    RESERVADA = "RESERVADA"
    EMITIDA = "EMITIDA"
    UTILIZADA = "UTILIZADA"


class EstadoVenta(str, enum.Enum):
    PENDIENTE = "PENDIENTE"
    PAGADA = "PAGADA"
    CANCELADA = "CANCELADA"


class Lugar(Base):
    __tablename__ = "lugares"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String)

    sectores = relationship("Sector", back_populates="lugar")
    eventos = relationship("Evento", back_populates="lugar")


class Sector(Base):
    __tablename__ = "sectores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    capacidad_maxima = Column(Integer, nullable=False)
    lugar_id = Column(Integer, ForeignKey("lugares.id"), nullable=False)

    lugar = relationship("Lugar", back_populates="sectores")


class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha = Column(DateTime)
    lugar_id = Column(Integer, ForeignKey("lugares.id"), nullable=False)

    lugar = relationship("Lugar", back_populates="eventos")
    precios = relationship("PrecioSector", back_populates="evento")
    entradas = relationship("Entrada", back_populates="evento")


class PrecioSector(Base):
    """Precio de un sector para un evento en particular."""
    __tablename__ = "precios_sector"

    id = Column(Integer, primary_key=True, index=True)
    precio = Column(Float, nullable=False)
    evento_id = Column(Integer, ForeignKey("eventos.id"), nullable=False)
    sector_id = Column(Integer, ForeignKey("sectores.id"), nullable=False)

    evento = relationship("Evento", back_populates="precios")
    sector = relationship("Sector")


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String)

    ventas = relationship("Venta", back_populates="cliente")


class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    estado = Column(Enum(EstadoVenta), default=EstadoVenta.PENDIENTE, nullable=False)
    total = Column(Float, default=0)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="ventas")
    entradas = relationship("Entrada", back_populates="venta")


class Entrada(Base):
    __tablename__ = "entradas"

    id = Column(Integer, primary_key=True, index=True)
    codigo_qr = Column(String, unique=True, index=True)
    estado = Column(Enum(EstadoEntrada), default=EstadoEntrada.DISPONIBLE, nullable=False)
    hora_ingreso = Column(DateTime, nullable=True)
    evento_id = Column(Integer, ForeignKey("eventos.id"), nullable=False)
    sector_id = Column(Integer, ForeignKey("sectores.id"), nullable=False)
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=True)

    evento = relationship("Evento", back_populates="entradas")
    sector = relationship("Sector")
    venta = relationship("Venta", back_populates="entradas")
