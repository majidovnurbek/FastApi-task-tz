from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.lesson import create_lesson, get_lessons, get_lesson_by_id
from schemas.lesson import LessonCreate
from database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/lessons",
    tags=["lessons"]
)

# Yangi dars yaratish
@router.post("/", status_code=201)
async def create_new_lesson(lesson: LessonCreate, db: Session = Depends(get_db)):
    return create_lesson(db=db, lesson=lesson)

# Barcha darslarni olish
@router.get("/", response_model=List[LessonCreate])
async def get_all_lessons(db: Session = Depends(get_db)):
    return get_lessons(db)

# Darsni ID orqali olish
@router.get("/{lesson_id}", response_model=LessonCreate)
async def get_single_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = get_lesson_by_id(db, lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson
