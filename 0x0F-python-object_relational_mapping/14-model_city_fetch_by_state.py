#!/usr/bin/python3 
"""  prints all City objects from the database hbtn_0e_14_usa """ 
import sys 
from sqlalchemy import (create_engine) 
from model_city import Base, City 
from model_city import Base, State 
from sqlalchemy.orm import sessionmaker 
 
 
if __name__ == "__main__": 
    engine = create_engine( 
            'mysql+mysqldb://{}:{}@localhost/{}'. 
            format(sys.argv[1], sys.argv[2], sys.argv[3]), 
            pool_pre_ping=True) 
 
    Base.metadata.create_all(engine) 
    Session = sessionmaker(bind=engine) 
    session = Session() 
 
    for C_id, C_name, S_name in session.query( 
            City.id, City.name, State.name).filter(State.id == City.state_id): 
        print(f"{S_name}: ({C_id}) {C_name}") 
