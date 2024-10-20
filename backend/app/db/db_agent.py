from sqlalchemy.orm import Session
from db.models import User, Character, Spell, Weapon, Consumable
from db.schemas import UserCreate, SpellCreate, CharacterCreate, WeaponCreate, ConsumableCreate
from db.session import Session, db_connection, Base
from faker import Faker

class DBAgent:
    def __init__(self):
        self.db = Session()
        self.engine = self.db.get_bind()

    def create_user(self, user: UserCreate):
        db_user = User(username=user.username, email=user.email, password=user.password)
        self.db.add(db_user)
        self.db.flush()
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def search_user(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def create_character(self, character: CharacterCreate):
        db_character = Character(name=character.name, level=character.level, user_id=character.user_id)
        self.db.add(db_character)
        self.db.flush()
        self.db.commit()
        return db_character

    def create_mock_data(self):
        fake = Faker(['en_US'])

        for _ in range(10): 
            user_data = {
            "username": str(fake.user_name()),
            "email": str(fake.email()),
            "password": str(fake.password())
            }
            user = UserCreate(**user_data)
            created_user = self.create_user(user)

            character_data = {
                "name": fake.name(),
                "level": 1,
                "user_id": created_user.id, 
            }
            character = CharacterCreate(**character_data)
            created_character = self.create_character(character)

    def clean_db(self):
        Base.metadata.drop_all(self.db.get_bind())
        self.db.commit()
        print("Database cleaned")

    def create_tables(self):
        print("Creating Tables...")
        try:
            Base.metadata.create_all(bind=self.engine)
            print("Tables created successfully!")
        except Exception as e:
            print("Tables failed to create.")
            print(e)


if __name__ == '__main__':
    agent = DBAgent()
    agent.clean_db()
    agent.create_tables()
    agent.create_mock_data()