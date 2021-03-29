#!/usr/bin/python3
"""
A script that changes the name of a State object
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    s = "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(s)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id.like(2)).first()
    state.name = "New Mexico"
    session.commit()
