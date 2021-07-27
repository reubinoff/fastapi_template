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
from fastapi_best_practice.models import OurBase

class Settings(Base):
    test = Column(String(16), primary_key=True, nullable=False)
    run_standalone = Column(Boolean)
    description = Column(String(50))


############################################################
class SettingsBase(OurBase):
    admin_mail: Optional[int]
    run_standalone: bool
    description: Optional[str]
 
class SettingsRead(SettingsBase):
    pass
