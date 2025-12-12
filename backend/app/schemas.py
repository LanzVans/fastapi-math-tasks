from pydantic import BaseModel, field_validator

class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str
    subject_id: int

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    question: str
    answer: str
    category_id: int

    @field_validator("question", mode="before")
    def escape_latex(cls, v):
        if isinstance(v, str):
            return v.replace("\\", "\\\\")
        return v

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    class Config:
        orm_mode = True