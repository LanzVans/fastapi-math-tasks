from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/subjects", tags=["subjects"])

@router.post("", response_model=schemas.Subject)
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    return crud.create_subject(db, subject)

@router.get("", response_model=list[schemas.Subject])
def list_subjects(db: Session = Depends(get_db)):
    return crud.get_subjects(db)

@router.delete("", response_model=list[schemas.Subject])
def delete_subject(id: int | None = None, db: Session = Depends(get_db)):
    return crud.delete_subject(db, id)