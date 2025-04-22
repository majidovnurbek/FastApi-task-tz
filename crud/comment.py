from sqlalchemy.orm import Session
from models.comment import Comment, Rating
from schemas.comment import CommentCreate, RatingCreate

# Izoh yaratish
def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# Baholash yaratish
def create_rating(db: Session, rating: RatingCreate):
    db_rating = Rating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
