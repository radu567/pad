from __future__ import unicode_literals
from sqlalchemy import (
    Column, String, Integer, Sequence, Float,
    create_engine,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import update

Base = declarative_base()

def get_connection_string(user, password, db, host='localhost', port=5432):
    '''
    Receives configuration params for the connection url, returns database connection string
    '''
    connection_string = 'postgresql://{username}:{password}@{host}:{port}/{db}'
    return connection_string.format(
        username=user,
        password=password,
        host=host,
        port=port,
        db=db,
    )

class Student(Base):
    '''
    Model based on sqlalchemy's Base
    '''
    __tablename__ = 'student'
    id = Column(Integer, Sequence(__tablename__ + '_seq'), primary_key=True)
    name = Column(String(250))
    mark = Column(Float)

def insert_student(db, name, mark):
    '''
    Creates a dummy object in the database
    '''
    student = Student()
    student.name = name
    student.mark = mark
    db.add(student)
    db.commit()

def update(db, id=0, mark=0):
    db.query(Student).filter_by(id=id).update({Student.mark: mark})

def delete(db, id=0):
    db.query(Student).filter(Student.id == id).delete()
    db.commit()

def query(db):
    '''
    Queries objects from the DB and prints retrieved objects
    '''
    result = db.query(Student).order_by(Student.name)
    for student in result:
        print('{}. {} - {}'.format(student.id, student.name, student.mark))


def main(create=True):
    """Entry point for the test script"""
    db_url = get_connection_string('postgres', '1', 'postgres')
    engine = create_engine(db_url, echo=True) # Set echo=False if you don't want output from the database driver in the console
    session_factory = sessionmaker(bind=engine)
    meta = Base.metadata
    if create:
        meta.create_all(engine)
    db_session = session_factory()
    #insert_student(db=db_session, name='Marcel', mark=9.5) #Uncomment to add some rows in database
    #update(db=db_session, id=2, mark=9.0) #Update mark
    #delete(db=db_session, id=1) #Uncomment to delete a row by id
    query(db=db_session)



if __name__ == '__main__':
    main()
