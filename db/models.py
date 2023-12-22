# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer, String, Boolean, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BaseModel = declarative_base()

task_subtask = Table(
    'task_subtask', BaseModel.metadata,
    Column('parent_id', Integer, ForeignKey('tasks.id'), primary_key=True),
    Column('child_id', Integer, ForeignKey('tasks.id'), primary_key=True)
)


class Task(BaseModel):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(String, nullable=False, default='Untitled')
    description = Column(String, nullable=True)
    urgent = Column(Boolean, nullable=False, default=True)
    major = Column(Boolean, nullable=False, default=True)
    deadline = Column(DateTime, nullable=True)

    subtasks = relationship(
        'Task',
        secondary=task_subtask,
        primaryjoin=id == task_subtask.c.parent_id,
        secondaryjoin=id == task_subtask.c.child_id,
    )
