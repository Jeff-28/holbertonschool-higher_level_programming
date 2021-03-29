#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    e = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                  argv[2],
                                                                  argv[3]))
    Session = sessionmaker(bind=e)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
