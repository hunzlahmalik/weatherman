from dataclasses import dataclass


@dataclass
class Weather:
    year: int
    month: int
    day: int
    temperature_max: float | None = None  # in Celsius
    temperature_mean: float | None = None
    temperature_min: float | None = None
    dew: float | None = None
    dew_mean: float | None = None
    dew_min: float | None = None
    humidity_max: float | None = None
    humidity_mean: float | None = None
    humidity_min: float | None = None
    pressure_max: float | None = None  # in hPa, sea level pressure
    pressure_mean: float | None = None
    pressure_min: float | None = None
    visibility_max: float | None = None  # in km
    visibility_mean: float | None = None
    visibility_min: float | None = None
    windspeed_max: float | None = None  # in km/h
    windspeed_mean: float | None = None
    gustspeed_max: float | None = None  # in km/h
    precipitation: float | None = None  # in mm
    cloudcover: float | None = None
    events: str | None = None
    wind_director: float | None = None  # in degrees
