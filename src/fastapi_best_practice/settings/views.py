from fastapi_versioning import version
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from fastapi_best_practice.database.core import get_db

from .models import SettingsCreate, SettingsRead, SettingsList
from .service import get_all, get, create

router = APIRouter()


@router.get("", response_model=SettingsList)
def get_settings(*, db_session: Session = Depends(get_db)):
    """
    Get a setting object.
    """
    settings = get_all(db_session=db_session)
    if not settings:
        raise HTTPException(status_code=404, detail="The settings does not exist.")
    return SettingsList(**settings).dict()

@router.get("/{settings_name}", response_model=str)
def get_settings_by_name(*, db_session: Session = Depends(get_db), settings_name: str):
    """
    Update a item.
    """
    item = get(db_session=db_session, setting_name=settings_name)
    if not item:
        raise HTTPException(status_code=404, detail="The items with this id does not exist.")
    return item.value



@router.post("", response_model=SettingsRead)
def add_settings(*, db_session: Session = Depends(get_db), settings_in: SettingsCreate):
    """
    Create a new product.
    """
    product = create(db_session=db_session, settings_in=settings_in)
    return product