#!/usr/bin/python3
''' contains the class definition of a State '''
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    ''' inherits from Base '''
    __tablename__ = 'states'
    id = Column(
            Integer, autoincrement=True, nullable=False,
            unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
