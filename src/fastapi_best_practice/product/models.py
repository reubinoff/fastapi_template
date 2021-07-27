from typing import List, Optional

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
    Table,
    Boolean,
    DateTime,
)
from fastapi_best_practice.database.core import Base
from fastapi_best_practice.models import BaseModel
from fastapi_best_practice.models import OurBase

class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    description = Column(String(50))


############################################################
class ProductBase(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
 
class ProductRead(ProductBase):
    id: Optional[int]

class ProductCreate(ProductBase):
    pass


class ProductPagination(BaseModel):
    total: int
    items: List[ProductRead] = []
