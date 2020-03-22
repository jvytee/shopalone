from typing import Union
from sqlalchemy import or_

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
