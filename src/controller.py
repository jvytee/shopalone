from datetime import datetime, timedelta

from typing import Union
from sqlalchemy import and_, or_

import database
from model import Node, Way, Visit


def get_market(market_id: int) -> Union[dict, None]:
    session = database.get_session()

    node = session.query(Node).filter(Node.id == market_id).first()
    if node is not None:
        return node

    way = session.query(Way).filter(Way.id == market_id).first()
    if way is not None:
        return way

    return None


def get_visits(market_id: int) -> Union[list, None]:
    session = database.get_session()

    visits = session.query(Visit).filter(or_(Visit.node_id == market_id, Visit.way_id == market_id)).all()
    return visits


def get_visits_at(market_id: int, timestamp: int) -> Union[list, None]:
    session = database.get_session()
    visit_datetime = datetime.fromtimestamp(timestamp)
    delta = timedelta(minutes=30)

    visits = (
        session.query(Visit)
        .filter(and_(or_(Visit.node_id == market_id, Visit.way_id == market_id), and_(Visit.tstamp < visit_datetime + delta, Visit.tstamp >= visit_datetime - delta)))
        .all()
    )

    return visits


def add_visit(market_id: int, timestamp: int):
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
