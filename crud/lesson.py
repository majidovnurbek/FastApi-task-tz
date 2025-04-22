from sqlalchemy.orm import Session
from models.lesson import Lesson
from schemas.lesson import LessonCreate

# Dars yaratish
def create_lesson(db: Session, lesson: LessonCreate):
    db_lesson = Lesson(title=lesson.title, content=lesson.content, video_url=lesson.video_url, course_id=lesson.course_id)
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

# Darslarni olish
def get_lessons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Lesson).offset(skip).limit(limit).all()

# Darsni ID orqali olish
def get_lesson_by_id(db: Session, lesson_id: int):
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()
