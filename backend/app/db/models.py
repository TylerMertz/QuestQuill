from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime
from pydantic import BaseModel

from app.db.session import Base

# User Table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    # Relationships
    characters = relationship("Character", back_populates="owner")

# Character Table
class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Relationships
    owner = relationship("User", back_populates="characters")
    spells = relationship("Spell", back_populates="character")
    weapons = relationship("Weapon", back_populates="character")
    consumables = relationship("Consumable", back_populates="character")

# Spell Table
class Spell(Base):
    __tablename__ = 'spells'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    damage = Column(Float, nullable=False)
    mana_cost = Column(Float, nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)

    # Relationships
    character = relationship("Character", back_populates="spells")

# Weapon Table
class Weapon(Base):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    attack_power = Column(Float, nullable=False)
    weight = Column(Float)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)

    # Relationships
    character = relationship("Character", back_populates="weapons")

# Consumable Table
class Consumable(Base):
    __tablename__ = 'consumables'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    effect = Column(Text, nullable=False)
    quantity = Column(Integer, default=1)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)

    # Relationships
    character = relationship("Character", back_populates="consumables")