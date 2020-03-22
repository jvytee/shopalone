from typing import Union

import database
import util
from model import Node, Way


def get_market(market_id: int) -> Union[dict, None]:
    session = database.get_session()

    node = session.query(Node).filter(Node.id == market_id).first()
    if node is not None:
        return {"id": node.id, "tags": node.tags, "location": util.to_list(node.geom)}

    way = session.query(Way).filter(Way.id == market_id).first()
    if way is not None:
        return {"id": way.id, "tags": way.tags, "location": list()}

    return None
