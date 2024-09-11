from sqlalchemy.orm import Session
from app.db.models import User, Character, Spell, Weapon, Consumable
from app.db.schemas import UserCreate, SpellCreate, CharacterCreate, WeaponCreate, ConsumableCreate
from app.db.session import Session, db_connection, Base
from faker import Faker

def create_user(user: UserCreate):
    db = Session()
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.flush()
    db.commit()
    db.refresh(db_user)
    return db_user

def create_character(character: CharacterCreate):
    db = Session()
    db_character = Character(name=character.name, level=character.level, user_id=character.user_id)
    db.add(db_character)
    db.flush()
    db.commit()
    return db_character

def create_mock_data():
    fake = Faker(['en_US'])

    for _ in range(10): 
        user_data = {
        "username": str(fake.user_name()),
        "email": str(fake.email()),
        "password": str(fake.password())
        }
        user = UserCreate(**user_data)
        created_user = create_user(user)

        character_data = {
            "name": fake.name(),
            "level": 1,
            "user_id": created_user.id, 
        }
        character = CharacterCreate(**character_data)
        created_character = create_character(character)

def clean_db(db):
    Base.metadata.drop_all(db.get_bind())
    db.commit()
    print("Database cleaned")

def create_tables(engine):
    print("Creating Tables...")
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully!")
    except Exception as e:
        print("Tables failed to create.")
        print(e)

#result = create_user(user)
def build_db():
    db = Session()
    engine = db.get_bind()

    clean_db(db)
    create_tables(engine)
    create_mock_data()

build_db()