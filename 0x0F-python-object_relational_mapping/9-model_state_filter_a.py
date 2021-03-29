#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
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

    que = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)
    for obj in que:
        print("{}: {}".format(obj.id, obj.name))
