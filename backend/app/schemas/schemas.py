from typing import Optional
from pydantic import BaseModel, field_validator

class SubjectBase(BaseModel):
    name: str
    
class Subject(SubjectBase):
    id: int
    class Config:
        orm_mode = True
   
class SubjectCreate(SubjectBase):
    pass




class CategoryBase(BaseModel):
    name: str
    subject_id: Optional[int] = None

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class CategoryCreate(CategoryBase):
    pass



class TaskBase(BaseModel):
    question: str
    answer: str
    category_id: Optional[int] = None

    @field_validator("question", mode="before")
    def escape_latex(cls, v):
        if isinstance(v, str):
            return v.replace("\\", "\\\\")
        return v

class Task(TaskBase):
    id: int
    class Config:
        orm_mode = True

class TaskCreate(TaskBase):
    pass

