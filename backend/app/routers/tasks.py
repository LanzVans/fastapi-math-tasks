from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get("", response_model=list[schemas.Task])
def list_tasks(category_id: int | None = None, db: Session = Depends(get_db)):
    return crud.get_tasks(db, category_id)