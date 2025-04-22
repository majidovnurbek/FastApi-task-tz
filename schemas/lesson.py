from pydantic import BaseModel
from typing import Optional

class LessonBase(BaseModel):
    title: str
    content: str
    video_url: str

class LessonCreate(LessonBase):
    course_id: int

class Lesson(LessonBase):
    id: int
    course_id: int

    class Config:
        orm_mode = True
