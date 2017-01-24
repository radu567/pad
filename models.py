from sqlalchemy import (
    Column, String, Integer, Float, Sequence,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    '''
    Model based on sqlalchemy's Base
    '''
    __tablename__ = 'student'
    id = Column(Integer, Sequence(__tablename__ + '_seq'), primary_key=True)
    name = Column(String(250))
    mark = Column(Float)
