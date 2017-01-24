from __future__ import unicode_literals
from sqlalchemy import (
    Column, String, Integer, Sequence,
    create_engine,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


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


class Slaim(Base):
    '''
    Model based on sqlalchemy's Base
    '''
    __tablename__ = 'slaim'
    id = Column(Integer, Sequence(__tablename__ + '_seq'), primary_key=True)
    name = Column(String(250))
    country = Column(String(64))


def create_slaims(db):
    '''
    Creates a dummy object in the database
    '''
    slaim = Slaim()
    slaim.name = 'Whatever'
    slaim.country = 'MD'
    db.add(slaim)
    db.commit()


def query_slaims(db):
    '''
    Queries objects from the DB and prints retrieved objects
    '''
    query = db.query(Slaim).order_by(Slaim.name)
    for slaim in query:
        print('{} - {}'.format(slaim.name, slaim.country))


def main(create=True):
    """Entry point for the test script"""
    db_url = get_connection_string('postgres', '1', 'postgres')
    engine = create_engine(db_url, echo=True) # Set echo=False if you don't want output from the database driver in the console
    session_factory = sessionmaker(bind=engine)
    meta = Base.metadata
    if create:
        meta.create_all(engine)
    db_session = session_factory()
    create_slaims(db=db_session)
    query_slaims(db=db_session)



if __name__ == '__main__':
    main()
