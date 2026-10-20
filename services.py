from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import schemas
from repository import UserRepository

class UserService:

    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate):
        existing_user = UserRepository.get_by_email(db, user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return UserRepository.create(db, user)

    @staticmethod
    def get_users(db: Session, skip: int, limit: int):
        return UserRepository.get_all(db, skip, limit)

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def update_user(db: Session, user_id: int, updated_user: schemas.UserCreate):
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserRepository.update(db, user_id, updated_user)

    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        UserRepository.delete(db, user)
        return None