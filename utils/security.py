from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os

# Parolni shifrlash uchun CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT sozlamalari
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")  # .env fayldan maxfiy kalitni olish
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token muddati

# Parolni shifrlash
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Parolni tekshirish
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# JWT token yaratish
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)  # Default: 15 daqiqa
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Tokenni validatsiya qilish
def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
