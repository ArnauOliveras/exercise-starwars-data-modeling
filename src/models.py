import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favoritos_personajes = Table(
    'favoritos_personajes', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuario.id'), primary_key=True),
    Column('personaje_id', Integer, ForeignKey('personaje.id'), primary_key=True)
)

favoritos_planetas = Table(
    'favoritos_planetas', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuario.id'), primary_key=True),
    Column('planeta_id', Integer, ForeignKey('planeta.id'), primary_key=True)
)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    fecha_suscripcion = Column(DateTime, nullable=False)
    
    favoritos_personajes = relationship('Personaje', secondary=favoritos_personajes, back_populates='usuarios_favoritos')
    favoritos_planetas = relationship('Planeta', secondary=favoritos_planetas, back_populates='usuarios_favoritos')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especie = Column(String(100))
    genero = Column(String(50))
    altura = Column(String(50))
    peso = Column(String(50))
    
    usuarios_favoritos = relationship('Usuario', secondary=favoritos_personajes, back_populates='favoritos_personajes')

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    clima = Column(String(100))
    terreno = Column(String(100))
    poblacion = Column(String(100))
    
    usuarios_favoritos = relationship('Usuario', secondary=favoritos_planetas, back_populates='favoritos_planetas')

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    contenido = Column(String(500), nullable=False)
    fecha_creacion = Column(DateTime, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    
render_er(Base, 'diagram.png')