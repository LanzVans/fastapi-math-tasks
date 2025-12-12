from sqlalchemy.orm import Session
from app import models, schemas

# SUBJECTS
def create_subject(db: Session, data: schemas.SubjectCreate):
    obj = models.Subject(name=data.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_subjects(db: Session):
    return db.query(models.Subject).all()


# CATEGORIES
def create_category(db: Session, data: schemas.CategoryCreate):
    obj = models.Category(name=data.name, subject_id=data.subject_id)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_categories(db: Session, subject_id: int = None):
    q = db.query(models.Category)
    if subject_id:
        q = q.filter(models.Category.subject_id == subject_id)
    return q.all()


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