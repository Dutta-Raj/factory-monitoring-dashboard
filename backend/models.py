from sqlalchemy import Column, Integer, String, Float
from database import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(String)
    name = Column(String)


class Workstation(Base):
    __tablename__ = "workstations"

    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(String)
    name = Column(String)


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    worker_id = Column(String)
    workstation_id = Column(String)
    event_type = Column(String)
    confidence = Column(Float)
    count = Column(Integer)