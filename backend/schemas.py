from pydantic import BaseModel

from enums import Priority

class TodoBase(BaseModel):
    priority: Priority
    description: str

class Todo(TodoBase):
    id: int 

    class Config:
        from_attributes = True

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass