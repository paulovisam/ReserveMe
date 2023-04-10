from pydantic import BaseModel
from typing import Any
class ReserveBase(BaseModel):
    hardware_id: int
    name_teacher: str
    loan_date: Any
    return_date: Any
    comments: str
    class Config:
        orm_mode = True
class ReserveUpdate(ReserveBase):
    id: int

class ReserveInDBBase(ReserveUpdate):
    hardware: Any