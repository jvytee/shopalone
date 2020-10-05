from sqlalchemy import Column, BigInteger, Integer, DateTime, Float
from sqlalchemy.dialects.postgresql import HSTORE, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

from . import util

Base = declarative_base()


class Node(Base):
    __tablename__ = "nodes"
    id = Column(BigInteger, primary_key=True)
    version = Column(Integer)
    user_id = Column(Integer)
    tstamp = Column(DateTime)
    changeset_id = Column(BigInteger)
    tags = Column(HSTORE)
    geom = Column(Geometry("POINT"))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "version": self.version,
            "user_id": self.user_id,
            "tstamp": self.tstamp.timestamp(),
            "changeset_id": self.changeset_id,
            "tags": self.tags,
            "geom": util.to_list(self.geom),
        }


class Way(Base):
    __tablename__ = "ways"
    id = Column(BigInteger, primary_key=True)
    version = Column(Integer)
    user_id = Column(Integer)
    tstamp = Column(DateTime)
    changeset_id = Column(BigInteger)
    tags = Column(HSTORE)
    nodes = Column(ARRAY(BigInteger))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "version": self.version,
            "user_id": self.user_id,
            "tstamp": self.tstamp.timestamp(),
            "changeset_id": self.changeset_id,
            "tags": self.tags,
            "nodes": self.nodes,
        }


class WayNode(Base):
    __tablename__ = "way_nodes"
    way_id = Column(BigInteger, primary_key=True)
    sequence_id = Column(Integer, primary_key=True)
    node_id = Column(BigInteger)

    def to_dict(self) -> dict:
        return {
            "way_id": self.way_id,
            "sequence_id": self.sequence_id,
            "node_id": self.node_id,
        }


class Visit(Base):
    __tablename__ = "visits"
    id = Column(BigInteger, primary_key=True)
    node_id = Column(BigInteger)
    way_id = Column(BigInteger)
    tstamp = Column(DateTime)
    weight = Column(Float)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "node_id": self.node_id,
            "way_id": self.way_id,
            "tstamp": self.tstamp.timestamp(),
            "weight": self.weight,
        }
