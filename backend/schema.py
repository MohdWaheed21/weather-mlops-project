from pydantic import BaseModel


class WeatherInput(BaseModel):
    Location: int
    Temp9am: float
    Humidity9am: float
    Pressure9am: float
    RainToday: int