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
    id = Column(Integer, primary_key=True)
    key = Column(String(32))
    value = Column(String(100))


############################################################
class SettingsBase(OurBase):
    id: Optional[int]
    key: str
    value: str

class SettingsCreate(SettingsBase):
    pass

class SettingsRead(SettingsBase):
    id: int
    def get_value(self):
        return self.value


class SettingsList(OurBase):
    items: List[SettingsRead] = []