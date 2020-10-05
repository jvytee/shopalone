"""Controller functions to abstract away database operations.
This is one (not too) big file since there are not many models yet.
If the application grows, this needs to be refactored into a package on its own."""

from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import and_, or_

from . import database
from .model import Node, Way, Visit


def get_market(market_id: int) -> Optional[dict]:
    session = database.get_session()

    node = session.query(Node).filter(Node.id == market_id).first()
    if node is not None:
        return node

    way = session.query(Way).filter(Way.id == market_id).first()
    if way is not None:
        return way

    return None


def get_visits(market_id: int) -> Optional[dict]:
    session = database.get_session()

    visits = session.query(Visit).filter(or_(Visit.node_id == market_id, Visit.way_id == market_id)).all()
    return visits


def get_visits_time(market_id: int, timestamp: int) -> Optional[dict]:
    session = database.get_session()
    visit_datetime = datetime.fromtimestamp(timestamp)
    delta = timedelta(minutes=30)

    visits = (
        session.query(Visit)
        .filter(
            and_(
                or_(Visit.node_id == market_id, Visit.way_id == market_id),
                and_(Visit.tstamp < visit_datetime + delta, Visit.tstamp >= visit_datetime - delta),
            )
        )
        .all()
    )

    return visits


def add_visit(market_id: int, timestamp: int) -> Optional[Visit]:
    session = database.get_session()

    node_id, way_id = None, None
    node = session.query(Node).filter(Node.id == market_id).first()
    if node is not None:
        node_id = market_id
    else:
        way = session.query(Way).filter(Way.id == market_id).first()
        if way is not None:
            way_id = market_id
        else:
            return None

    visit = Visit(node_id=node_id, way_id=way_id, tstamp=datetime.fromtimestamp(timestamp), weight=1.0)
    session.add(visit)
    session.commit()

    return visit


def get_postcode(code: str) -> Optional[list]:
    session = database.get_session()

    nodes = session.query(Node).filter(Node.tags["addr:postcode"] == code).all()
    ways = session.query(Way).filter(Way.tags["addr:postcode"] == code).all()

    return nodes + ways
