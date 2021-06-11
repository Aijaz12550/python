import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true     
from sqlalchemy.orm import session, sessionmaker   

Base = declarative_base()


class Models() :
    __tablename__ = "users"

    def __init__(self):

        self.users = {
        "id": Column(Integer, primary_key=true),
        "name": Column(String, )
        }


if __name__ == "__main__":
    engine = create_engine('sql+sqllite:///localhost:3306')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
