from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String, unique=True, index=True)
    elements = relationship("Element", back_populates="device")

class Element(Base):
    __tablename__ = "elements"

    id = Column(String, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    avg_before_norm = Column(Float)
    avg_after_norm = Column(Float)
    data_size = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    device = relationship("Device", back_populates="elements")