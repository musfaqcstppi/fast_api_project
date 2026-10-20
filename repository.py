from sqlalchemy.orm import Session
import models, schemas

class UserRepository:
    
    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    @staticmethod
    def get_by_id(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, user: schemas.UserCreate):
        db_user = models.User(name=user.name, email=user.email, age=user.age)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update(db: Session, user_id: int, updated_data: schemas.UserCreate):
        user_query = db.query(models.User).filter(models.User.id == user_id)
        user_query.update(updated_data.model_dump(), synchronize_session=False)
        db.commit()
        return user_query.first()

    @staticmethod
    def delete(db: Session, user):
        db.delete(user)
        db.commit()