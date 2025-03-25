from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
