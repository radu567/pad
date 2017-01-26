from __future__ import unicode_literals
from bottle.bottle import route, run, template, error, redirect
from sqlalchemy import (
    Column, String, Integer, Sequence,
    create_engine, MetaData
)
import json
from .models import Student

from sqlalchemy.orm import sessionmaker, class_mapper
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

def query(db, table, order=False, criterion=False):
    '''
    Queries objects from the DB and prints retrieved objects
    '''
    result = db.query(Student).order_by(Student.name)
    for student in result:
        print('{} - {}'.format(student.name, student.mark))
    return result

def get_model(engine, table_name):
  meta = MetaData()
  meta.reflect(bind=engine)
  table = meta.tables[table_name]
  return table

def serialize(model):
  """Transforms a model into a dictionary which can be dumped to JSON."""
  # first we get the names of all the columns on model
  columns = [c.key for c in class_mapper(model.__class__).columns]
  # then we return their values in a dict
  return dict((c, getattr(model, c)) for c in columns)

@route('/student', method='GET')
def index():
    table_name = "student"
    db_url = get_connection_string('postgres', '1', 'postgres')
    engine = create_engine(db_url, echo=True) # Set echo=False if you don't want output from the database driver in the console
    session_factory = sessionmaker(bind=engine)
    db_session = session_factory()
    serialized_data = [
      serialize(row)
      for row in query(db=db_session, table=get_model(engine, table_name))
    ]
    json_obj = json.dumps(serialized_data)
    return json_obj

@route('/index')
def wrong():
    redirect("/student")

@error(404)
def error404(error):
    return 'Page not found'

def main(port_server):
    run(host='localhost', port=port_server, debug=True)
