import re
import functools
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker, object_session
from sqlalchemy.sql.expression import true
from sqlalchemy_utils import get_mapper
from starlette.requests import Request

from fastapi_best_practice.config import configuration


engine = create_engine(str(configuration.sql_uri))
SessionLocal = sessionmaker(bind=engine)


def resolve_table_name(name):
    """Resolves table names to their mapped names."""
    names = re.split("(?=[A-Z])", name)  # noqa
    return "_".join([x.lower() for x in names if x])


raise_attribute_error = object()


def resolve_attr(obj, attr, default=None):
    """Attempts to access attr via dotted notation, returns none if attr does not exist."""
    try:
        return functools.reduce(getattr, attr.split("."), obj)
    except AttributeError:
        return default


class CustomBase:
    @declared_attr
    def __tablename__(self):
        return resolve_table_name(self.__name__)


Base = declarative_base(cls=CustomBase)


def get_db(request: Request):
    return request.state.db
