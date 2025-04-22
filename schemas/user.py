from pydantic import BaseModel, EmailStr

# Register uchun schema
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str

# Login uchun schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Foydalanuvchi ma'lumotlarini o'qish uchun schema
class UserRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True
