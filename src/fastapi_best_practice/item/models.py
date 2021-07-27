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


############################################################
# SQL models...
############################################################
class Item(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    description = Column(String(50))


############################################################
# Pydantic models...
############################################################
class ItemBase(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
 
class ItemRead(ItemBase):
    id: Optional[int]

class ItemCreate(ItemBase):
    pass


class ItemPagination(BaseModel):
    total: int
    items: List[ItemRead] = []
