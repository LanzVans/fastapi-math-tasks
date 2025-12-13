from fastapi import FastAPI
from app.database import engine, Base
from app.routers import subjects, categories, tasks
from fastapi.middleware.cors import CORSMiddleware





# Tworzenie tabel
'''Base.metadata.create_all(bind=engine)'''

app = FastAPI(title="Math Tasks API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # jeśli wolisz: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rejestracja routerów
app.include_router(subjects.router)
app.include_router(categories.router)
app.include_router(tasks.router)