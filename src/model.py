from sqlalchemy import Column, BigInteger, Integer, Time
from sqlalchemy.dialects.postgresql import HSTORE, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()


class Node(Base):
    __tablename__ = "nodes"
    id = Column(BigInteger, primary_key=True)
    version = Column(Integer)
    user_id = Column(Integer)
    tstamp = Column(Time)
    changeset_id = Column(BigInteger)
    tags = Column(HSTORE)
    geom = Column(Geometry("POINT"))


class Way(Base):
    __tablename__ = "ways"
    id = Column(BigInteger, primary_key=True)
    version = Column(Integer)
    user_id = Column(Integer)
    tstamp = Column(Time)
    changeset_id = Column(BigInteger)
    tags = Column(HSTORE)
    nodes = Column(ARRAY(BigInteger))


class WayNode(Base):
    __tablename__ = "way_nodes"
    way_id = Column(BigInteger, primary_key=True)
    sequence_id = Column(Integer, primary_key=True)
    node_id = Column(BigInteger)
