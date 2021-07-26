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

class Settings(Base):
    admin_mail = Column(String, primary_key=True)
    run_standalone = Column(Boolean)
    description = Column(String)


############################################################
class SettingsBase(BaseModel):
    admin_mail: Optional[int]
    run_standalone: bool
    description: Optional[str]
 
class SettingsRead(SettingsBase):
    pass
