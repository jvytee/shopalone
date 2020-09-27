import os

import click
from flask import g
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .model import Base


def get_engine():
    if "engine" not in g:
        username = os.environ.get("PG_USERNAME", "postgres")
        password = os.environ.get("PG_PASSWORD", "postgres")
        host = os.environ.get("PG_HOST", "localhost")
        port = os.environ.get("PG_PORT", "5432")
        schema = os.environ.get("PG_SCHEMA", "shopalone")

        url = f"postgresql://{username}:{password}@{host}:{port}/{schema}"
        g.engine = create_engine(url)

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
