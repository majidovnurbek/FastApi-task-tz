from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.comment import create_comment, create_rating
from schemas.comment import CommentCreate, RatingCreate
from database import SessionLocal

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

# Izoh yaratish
@router.post("/", status_code=201)
async def create_new_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return create_comment(db=db, comment=comment)

# Baholash yaratish
@router.post("/rating", status_code=201)
async def create_new_rating(rating: RatingCreate, db: Session = Depends(get_db)):
    return create_rating(db=db, rating=rating)
