from dataclasses import dataclass


@dataclass
class Weather:
    temperature_max: float | None = None  # in Celsius
    temperature_mean: float | None = None
    temperature_min: float | None = None
    humidity_max: float | None = None
    humidity_mean: float | None = None
    humidity_min: float | None = None
