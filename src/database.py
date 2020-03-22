import click
from flask import g
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base


def get_engine():
    if "engine" not in g:
        g.engine = create_engine("postgresql://postgres:postgres@127.0.0.1/shopalone")

    return g.engine


def get_session():
    if "orm_session" not in g:
        g.orm_session = sessionmaker(bind=get_engine())

    return g.orm_session()


def close_session(e=None):
    session = g.pop("session", None)

    if session is not None:
        session.close()


@click.command("init-db")
@with_appcontext
def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
