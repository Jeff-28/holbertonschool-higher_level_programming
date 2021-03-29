#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    s = "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(s)
    Session = sessionmaker(bind=engine)
    session = Session()

    que = session.query(State, City).filter(State.id == City.state_id)\
                                    .order_by(City.id)
    for obj in que:
        print("{}: ({}) {}".format(obj.State.name, obj.City.id, obj.City.name))
