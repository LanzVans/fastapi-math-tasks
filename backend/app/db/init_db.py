from app.db.database import Base, engine
from app.models.models import Task, Subject, Category
Base.metadata.create_all(bind=engine)