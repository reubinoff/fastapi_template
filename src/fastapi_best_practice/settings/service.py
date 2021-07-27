import functools

from typing import  Any, Optional, List

from pydantic.types import StrBytes

from .models import Settings, SettingsCreate


def get_all(*, db_session) -> Optional[Settings]:
    """Returns all items."""
    return {"items": db_session.query(Settings).all()}


def get(*, db_session, setting_name: str) -> Optional[Settings]:
    """Returns a value of ."""
    return _get_settings_by_name(db_session=db_session, setting_name=setting_name)

def _get_settings_by_name(db_session, setting_name: str) -> Optional[Any]:
    if setting_name is None or isinstance(setting_name, str) is False:
        raise ValueError("The Valuse of setting name cannot be None")
    result =  db_session.query(Settings).filter(Settings.key == setting_name).one_or_none()
    if result is None:
        return None
    
    return result


def create(*, db_session, settings_in: SettingsCreate) -> Settings:
    settings = Settings(**settings_in.dict())

    db_session.add(settings)
    db_session.commit()
    return settings