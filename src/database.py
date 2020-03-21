from flask import current_app, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    if 'engine' not in g:
        g.engine = create_engine('postgresql://postgres:postgres@127.0.0.1/shopalone')

    return g.engine


def get_session():
    if 'orm_session' not in g:
        g.orm_session = sessionmaker(bind=get_engine())

    return g.orm_session()