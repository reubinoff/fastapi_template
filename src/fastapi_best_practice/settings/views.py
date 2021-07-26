from fastapi_versioning import version
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from fastapi_best_practice.database.core import get_db

from .models import SettingsRead
from .service import get_all

router = APIRouter()


@router.get("", response_model=SettingsRead)
def get_settings(*, db_session: Session = Depends(get_db), item_id: int):
    """
    Get a setting object.
    """
    settings = get_all(db_session=db_session)
    if not settings:
        raise HTTPException(status_code=404, detail="The settings does not exist.")
    return settings
