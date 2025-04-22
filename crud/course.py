from sqlalchemy.orm import Session
from models.course import Course
from schemas.course import CourseCreate

# Kurs qo'shish
def create_course(db: Session, course: CourseCreate, author_id: int):
    db_course = Course(title=course.title, description=course.description, author_id=author_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# Kurslarni olish
def get_courses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Course).offset(skip).limit(limit).all()

# Kursni ID orqali olish
def get_course_by_id(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()
