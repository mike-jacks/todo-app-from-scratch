from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum as SQLEnum
from database import Base

from enums import Priority


class Todo(Base):
    __tablename__ = "todo"

    id: int =  Column(Integer, primary_key=True)
    priority: Priority = Column(SQLEnum(Priority, name="priority"), nullable=False)
    description: str = Column(String)