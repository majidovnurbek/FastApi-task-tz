from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from models import course  # Modelni import qilish
from schemas.course import CourseCreate, CourseResponse  # Schema'larni import qilish
from database import get_db
from routers.auth import get_current_user

router = APIRouter(prefix="/courses", tags=["courses"])

@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_new_course(
    course: CourseCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    # Kurs yaratish logikasi
    new_course = course(
        title=course.title,
        description=course.description,
        author_id=current_user['id']  # current_user'dan author_id olish
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course
