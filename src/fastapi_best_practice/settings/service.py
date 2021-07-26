import functools

from typing import  Any, Optional, List

from pydantic.types import StrBytes

from .models import Settings


def get_all(*, db_session) -> Optional[Settings]:
    """Returns all items."""
    return db_session.query(Settings)


def get(*, db_session, setting_name: str) -> Optional[Settings]:
    """Returns a value of ."""
    _get_settings_by_name(db_session=db_session, setting_name=setting_name)

def _get_settings_by_name(db_session, setting_name: str) -> Optional[Any]:
    result =  db_session.query(Settings)
    if result is None:
        return None
    if setting_name is None or isinstance(setting_name, str) is False:
        raise ValueError("The Valuse of setting name cannot be None")
    setting_val = getattr(result, setting_name, None)
    return setting_val