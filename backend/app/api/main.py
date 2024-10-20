from fastapi import FastAPI , HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field
from typing import List
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from db.db_agent import DBAgent
from db.schemas import UserCreate, UserBase
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext

app = FastAPI()

#Intitialize encrypter
password_context = CryptContext(schemes='bcrypt', deprecated="auto")

#JWT secret and algo
SECRET_KEY = "secret_token"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#oauth2 scheme for token authentication
ouath2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow all origins (Not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(input_password: str, hashed_password: str) -> bool:
    return password_context.verify(input_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta| None = None):
    now = datetime.now()

    #USe default 15 minutes if none provided 
    if expires_delta is None:
        expires_delta = timedelta(minutes=30)

    #Set expiration time
    expire = datetime.now(timezone.utc) + expires_delta
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(data: UserCreate):

    print(f"FRONTEND PACKAGE: {data}")

    data.password = hash_password(data.password)

    try:
        agent = DBAgent()
        agent.create_user(data)
    except Exception as e:
        print(f"Error creating user: {e}")

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginCredentials(BaseModel):
    username: str
    password: str

@app.post("/login", response_model=Token)
async def login_user(data: LoginCredentials):
    agent = DBAgent()

    user = agent.search_user(data.username)

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=400, detail="Incorrect email or password. Try again"
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
    # try:
    #     agent.clean_db()
    #     agent.create_tables()
    #     return {"access_token": "Success", "token_type": "Bearer"}
    # except Exception as e:
    #     print(f"Error building db: {e}")
    #     return {"access_token": "Failure", "token_type": "Bearer"}

@app.get("/users/me", response_model=UserBase)
async def fetch_user(token: str = Depends(ouath2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Username not found in decrypted token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Failed to decode payload.")
        #raise HTTPException(status_code=401, detail="Invalid Credentials!!!")
    
    agent = DBAgent()
    user = agent.search_user(username)
    if user is None:
        raise HTTPException(status_code=401, detail="user not found in database.")
    
    return UserBase(username=user.username, email=user.email)