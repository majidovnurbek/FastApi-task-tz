from pydantic import BaseModel

class CommentBase(BaseModel):
    text: str
    lesson_id: int
    user_id: int

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int

    class Config:
        orm_mode = True


class RatingBase(BaseModel):
    stars: int
    lesson_id: int
    user_id: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int

    class Config:
        orm_mode = True
