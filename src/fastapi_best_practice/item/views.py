from fastapi_versioning import version
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session


from fastapi_best_practice.models import OurBase
from fastapi_best_practice.database.core import get_db
from fastapi_best_practice.database.services import common_parameters, search_filter_sort_paginate

from .models import ItemCreate, ItemRead
from .service import create, get

router = APIRouter()


@router.get("", response_model=OurBase)
@version(1)
def get_items(*, common: dict = Depends(common_parameters)):
    """
    Get all item.
    """
    return search_filter_sort_paginate(model="Item", **common)


@router.get("/{item_id}", response_model=ItemRead)
@version(2)
def get_item(*, db_session: Session = Depends(get_db), item_id: int):
    """
    Update a item.
    """
    item = get(db_session=db_session, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="The items with this id does not exist.")
    return item


@router.post("", response_model=ItemCreate)
@version(1.1)
def create_item(*, db_session: Session = Depends(get_db), item_in: ItemCreate):
    """
    Create a new item.
    """
    item = create(db_session=db_session, item_in=item_in)
    return item
