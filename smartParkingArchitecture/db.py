from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime


Base = declarative_base()

engine = create_engine(
    "mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost/parking_system",
    echo=True
)


Session = sessionmaker(bind=engine)
session = Session()


class Resident(Base):
    __tablename__ = 'residents'

    id = Column(Integer, primary_key=True)
    plate = Column(String(20), nullable=False)

class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True)
    plate = Column(String(20), nullable=False)
    entry_time = Column(DateTime, default=datetime.utcnow)
    exit_time = Column(DateTime, nullable=True)


Base.metadata.create_all(engine)

print("Veritabanı ve tablolar başarıyla oluşturuldu!")


