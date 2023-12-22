# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from . import models


class Database:
    __engine = sqlalchemy.create_engine(f'sqlite:///db.sqlite', echo=False)

    models.BaseModel.metadata.create_all(__engine)

    Session = sessionmaker(bind=__engine)
