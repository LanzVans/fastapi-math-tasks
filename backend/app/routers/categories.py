from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("", response_model=schemas.Category)
def create_category(cat: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, cat)

@router.get("", response_model=list[schemas.Category])
def list_categories(subject_id: int | None = None, db: Session = Depends(get_db)):
    return crud.get_categories(db, subject_id)