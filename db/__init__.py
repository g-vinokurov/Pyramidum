# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from . import models

from .models import KanbanStatus


class Database:
    __engine = sqlalchemy.create_engine(f'sqlite:///db.sqlite', echo=False)

    models.BaseModel.metadata.create_all(__engine)

    Session = sessionmaker(bind=__engine)

    with Session() as session:
        if not session.query(KanbanStatus).filter_by(title='Backlog').first():
            session.add(KanbanStatus(title='Backlog'))
        session.commit()


# session = Database.Session()
#
# backlog = session.query(KanbanStatus).filter_by(title='Backlog').first()
#
# task1 = Task(title='Task #1', kanban_status=backlog)
# task2 = Task(title='Task #1.1', kanban_status=backlog)
# task1.subtasks = [task2]
# session.add(task1)
# session.add(task2)
# session.commit()
#
# print(task1.subtasks)
# print(task1.kanban_status.title)
# print(task2.kanban_status.title)
