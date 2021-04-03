#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    s = "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(s)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    state.cities = [City(name="San Francisco")]
    session.add(state)
    session.commit()
    session.close()
