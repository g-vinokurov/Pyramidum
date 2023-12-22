# -*- coding: utf-8 -*-

from db import Database
from db.models import Task


class TaskManager:
    @staticmethod
    def get_all():
        with Database.Session() as session:
            return session.query(Task).all()
