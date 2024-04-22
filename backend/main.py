import json

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas, crud

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # The origin of the frontend app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

todos: list[schemas.Todo] = []

@app.get("/todos", response_model=list[schemas.Todo])
async def get_todos(db: Session = Depends(get_db)) -> list[schemas.Todo]:
    return crud.get_todos(db=db)

@app.post("/todos", response_model=schemas.Todo)
async def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)) -> schemas.Todo:
    print(json.dumps(todo.model_dump(), indent=4))
    return crud.create_todo(db=db, todo=todo)

@app.put("/todos/{todo_id}", response_model=schemas.Todo)
async def update_todo(todo: schemas.TodoUpdate, todo_id: int, db: Session = Depends(get_db)) -> schemas.Todo:
    return crud.update_todo(db=db, todo_id=todo_id, todo=todo)

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> None:
    return crud.delete_todo(db=db, todo_id=todo_id)
