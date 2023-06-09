from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models import user as  users_models
from schemas import user as users_schemas
from utils import crud
from config.db import SessionLocal, engine

users_models.Base.metadata.create_all(bind=engine)

user_router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.post("/users/", response_model=users_schemas.User)
def create_user(user: users_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@user_router.get("/users/", response_model=list[users_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@user_router.get("/users/{user_id}", response_model=users_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.post("/users/{user_id}/items/", response_model=users_schemas.Item)
def create_item_for_user(
    user_id: int, item: users_schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@user_router.get("/items/", response_model=list[users_schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items