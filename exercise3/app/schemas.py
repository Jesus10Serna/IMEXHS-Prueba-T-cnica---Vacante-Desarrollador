from pydantic import BaseModel, constr
from typing import List, Dict, Any
from datetime import datetime

class DeviceBase(BaseModel):
    device_name: str

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int

    class Config:
        orm_mode = True

class ElementBase(BaseModel):
    id: str
    data: List[str]
    deviceName: str

class ElementCreate(BaseModel):
    elements: Dict[str, ElementBase]

class ElementUpdate(BaseModel):
    device_name: str = None
    id: str = None

class Element(BaseModel):
    id: str
    device_id: int
    avg_before_norm: float
    avg_after_norm: float
    data_size: int
    created_date: datetime
    updated_date: datetime
    device: Device

    class Config:
        orm_mode = True