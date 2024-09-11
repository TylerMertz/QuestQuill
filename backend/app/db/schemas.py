from pydantic import BaseModel
from typing import List, Optional

#Pydantic Models for User
class UserBase(BaseModel):
    username: str
    email: str
class UserCreate(UserBase):
    password: str
class UserResponse(UserBase):
    id: int
    characters: List['CharacterResponse'] = []  # List of characters related to the user

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models

# Pydantic Models for Character
class CharacterBase(BaseModel):
    name: str
    level: int
class CharacterCreate(CharacterBase):
    user_id: int

class CharacterResponse(CharacterBase):
    id: int
    spells: List['SpellResponse'] = []  # List of spells related to the character
    weapons: List['WeaponResponse'] = []  # List of weapons related to the character
    consumables: List['ConsumableResponse'] = []  # List of consumables related to the character

    class Config:
        orm_mode = True

# Pydantic Models for Spell
class SpellBase(BaseModel):
    name: str
    damage: float
    mana_cost: float
class SpellCreate(SpellBase):
    pass
class SpellResponse(SpellBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic Models for Weapon
class WeaponBase(BaseModel):
    name: str
    attack_power: float
    weight: Optional[float] = None
class WeaponCreate(WeaponBase):
    pass
class WeaponResponse(WeaponBase):
    id: int
    
    class Config:
        orm_mode = True

# Pydantic Models for Consumable
class ConsumableBase(BaseModel):
    name: str
    effect: str
    quantity: int
class ConsumableCreate(ConsumableBase):
    pass
class ConsumableResponse(ConsumableBase):
    id: int

    class Config:
        orm_mode = True