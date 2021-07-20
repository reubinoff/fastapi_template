from pydantic import BaseModel, validator



########################## SQLAlchemy models ##########################



#################################################################





########################## Pydantic models ##########################
class OurBase(BaseModel):
    class Config:
        orm_mode = True
        validate_assignment = True
        arbitrary_types_allowed = True
        anystr_strip_whitespace = True



#################################################################