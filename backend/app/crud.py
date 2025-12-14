from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app import models, schemas

# SUBJECTS
def create_subject(db: Session, data: list[schemas.SubjectCreate]):
    obj = [models.Subject(**subject.model_dump()) for subject in data]
    db.add_all(obj)
    db.commit()
    for subject in obj:
        db.refresh(subject)
    return obj

def get_subjects(db: Session):
    return db.query(models.Subject).all()


def delete_subject(db: Session, id: int = None):
    if id:
        obj=db.query(models.Subject).filter(models.Subject.id == id).first()
        db.delete(obj)
        db.commit()
    return db.query(models.Subject).all()


# CATEGORIES
def create_category(db: Session, data: list[schemas.CategoryCreate]):
    obj = [models.Category(**category.model_dump()) for category in data ]
    db.add_all(obj)
    db.commit()
    for category in obj:
        db.refresh(category)
    return obj

def get_categories(db: Session, subject_id: int = None):
    q = db.query(models.Category)
    if subject_id:
        q = q.filter(models.Category.subject_id == subject_id)
    return q.all()

def delete_categorie(db: Session, id: int = None):
    if id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Brak ID kategorii do usunięcia."
        )
    obj = db.query(models.Category).filter(models.Category.id == id).first()
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Kategoria o ID {id} nie istnieje."
        )
    db.delete(obj)
    db.commit()
    return db.query(models.Category).all()


# TASKS
def create_task(db: Session, data: schemas.TaskCreate):
    obj = models.Task(question=data.question, answer=data.answer, category_id=data.category_id)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_tasks(db: Session, category_id: int = None):
    q = db.query(models.Task)
    if category_id:
        q = q.filter(models.Task.category_id == category_id)
    return q.all()

def delete_task (db: Session, id: int =None):
    if id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Brak ID zadania do usunięcia.")
        
    obj=db.query(models.Task).filter(models.Task.id == id).first()
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_400_NOT_FOUND,
            detail=f"Zadanie o ID {id} nie istnieje."
        )
    db.delete(obj)
    db.commit()
    return db.query(models.Task).all()
            
            
        
        