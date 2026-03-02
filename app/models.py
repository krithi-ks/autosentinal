from sqlalchemy import Column, Integer, Float, String
from .database import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    engine_temp = Column(Float)
    oil_pressure = Column(Float)
    battery_voltage = Column(Float)
    speed = Column(Float)
    prediction = Column(String)
    priority = Column(String)