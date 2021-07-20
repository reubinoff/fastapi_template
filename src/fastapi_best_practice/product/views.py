from fastapi_versioning import version
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session


from fastapi_best_practice.models import OurBase
from fastapi_best_practice.database.core import get_db
from fastapi_best_practice.database.services import common_parameters, search_filter_sort_paginate

from .models import ProductCreate, ProductRead
from .service import create, get

router = APIRouter()


@router.get("", response_model=OurBase)
def get_products(*, common: dict = Depends(common_parameters)):
    """
    Get all product.
    """
    return search_filter_sort_paginate(model="Product", **common)

@router.get("", response_model=OurBase)
@version(2)
def get_products(*, common: dict = Depends(common_parameters)):
    """
    Get all product.
    """
    return {
        "test": "test"
    }

@router.get("/{product_id}", response_model=ProductRead)
def get_product(*, db_session: Session = Depends(get_db), product_id: int):
    """
    Update a product.
    """
    product = get(db_session=db_session, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="The products with this id does not exist.")
    return product


@router.post("", response_model=ProductCreate)
def create_product(*, db_session: Session = Depends(get_db), product_in: ProductCreate):
    """
    Create a new product.
    """
    product = create(db_session=db_session, product_in=product_in)
    return product

@router.delete("", response_model=ProductCreate)
def delete_product(*, db_session: Session = Depends(get_db), product_in: ProductCreate):
    """
    Delete a product.
    """
    return "OK"