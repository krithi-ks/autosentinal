from pydantic import BaseModel

class Telemetry(BaseModel):
    engine_temp: float
    oil_pressure: float
    battery_voltage: float
    brake_status: int
    speed: float