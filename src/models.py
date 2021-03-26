import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    Username = Column(String(250))
    Firstname = Column(String(250))
    Password = Column(String(250))

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    age = Column(Integer)
    race = Column(String(250))

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    languaje = Column(String(250))
    

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), ForeignKey("user.username"))
    favorite_planet = Column(Integer, ForeignKey("planets.name"))
    favorite_character = Column(Integer, ForeignKey("character.name"))
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')