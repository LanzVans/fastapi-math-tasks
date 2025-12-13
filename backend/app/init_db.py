from database import Base, engine
from models import Task, Subject, Category
Base.metadata.create_all(bind=engine)