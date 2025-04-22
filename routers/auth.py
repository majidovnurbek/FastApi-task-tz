from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from models.user import User
from schemas.user import UserCreate, UserLogin, UserRead
from utils.security import hash_password, verify_password, create_access_token
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()  # .env faylni yuklaydi

# DB konfiguratsiyasi
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

router = APIRouter()

# OAuth2PasswordBearer uchun tokenni olish
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# DB sessiyasini olish
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Foydalanuvchi ro'yxatdan o'tishi
@router.post("/auth/register", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Email orqali foydalanuvchini tekshirish
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email allaqachon mavjud")

    # Yangi foydalanuvchini yaratish
    hashed_password = hash_password(user.password)
    db_user = User(full_name=user.full_name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

# Foydalanuvchi login qilishi va token olish
@router.post("/auth/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    # JWT token yaratish
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# Himoyalangan endpoint: Tokenni tekshirish
@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {"message": "Token is valid", "token": token}
