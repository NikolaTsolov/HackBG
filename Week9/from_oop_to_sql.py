from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from settings import DB_CONNECTION_STRING
from sqlalchemy import Session

Base = declarative_base()

class Person(Base):
    __tablename__ = "Peaople"
    id = Column(Integer, primery_key=True)
    name = Column(String(20))

engine = create_engine(DB_CONNECTION_STRING)
Base.metadata.create_all(engine)

session = Session(bind=engine)

kolio = Person(name="Kolio")

session.add(kolio)
seesion.commit()
