from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

todos: list[schemas.Todo] = []

@app.get("/", response_model=list[schemas.Todo])
async def get_todos(db: Session = Depends(get_db)) -> list[schemas.Todo]:
    return crud.get_todos(db=db)

@app.post("/", response_model=schemas.Todo)
async def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)) -> schemas.Todo:
    return crud.create_todo(db=db, todo=todo)

@app.delete("/")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> None:
    return crud.delete_todo(db=db, todo_id=todo_id)
