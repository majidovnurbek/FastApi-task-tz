from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True
