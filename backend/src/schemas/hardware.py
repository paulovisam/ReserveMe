from pydantic import BaseModel
from typing import Any
class HardwareBase(BaseModel):
    name: str
    description: str
    amount: int
    status: str
    class Config:
        orm_mode = True
class HardwareUpdate(HardwareBase):
    id: int

class HardwareInDBBase(HardwareUpdate):
    pass