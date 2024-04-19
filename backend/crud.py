from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

import models, schemas

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).one_or_none()
    if not db_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo ID: {todo_id} not found.")
    db.delete(db_todo)
    db.commit()