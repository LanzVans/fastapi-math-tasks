from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api import crud
from app.schemas import schemas

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("", response_model=list[schemas.Category])
def create_category(cat: list[schemas.CategoryCreate], db: Session = Depends(get_db)):
    return crud.create_category(db, cat)

@router.get("", response_model=list[schemas.Category])
def list_categories(subject_id: int | None = None, db: Session = Depends(get_db)):
    return crud.get_categories(db, subject_id)

@router.delete("/delete",response_model=list[schemas.Category])
def delete_category(id: int | None = None, db: Session = Depends(get_db)):
    return crud.delete_categorie(db, id)