from weatherman.utils import reader
from weatherman.constants import LOCATION, MONTHS
from weatherman import Weather


class WeatherMan:
    _dirpath: str = ""
    _cache: dict[str, dict[str, Weather]] = {}

    def __init__(self, dirpath: str) -> None:
        self._dirpath = dirpath

    def read_file(self, year: int, month: int) -> dict[str, Weather]:
        """ Reads a weather file and returns a dict of @Weather objects.

        Args:
            year (int): year of the weather
            month (int): month of the weather

        Returns:
            dict[str, Weather]: key is date in YYYY-MM-DD, value is Weather for day
        """

        return reader(
            (self._dirpath + "/" + LOCATION + "_weather_{}_{}.txt").format(
                year, MONTHS[month-1]
            )
        )

    def get_extremes(
        self, year: int, month: int = None, force_reload=False
    ) -> dict[str, dict[str, dict[str, str | float]]]:
        """ Get the extremes of the weather for a given year.

        Args:
            year (int): year of the weather
            month (int, optional): month of the weather. Defaults to None.
            force_reload (bool, optional): force reload of the cache. Defaults to False.

        Returns:
            dict[str, dict[str, dict[str, str | float]]]: Computed values

            e.g
            {
                "temperature": {
                    "heighest": {"date": "", "value": None},
                    "lowest": {"date": "", "value": None},
                },
                "humidity": {
                    "heighest": {"date": "", "value": None},
                    "lowest": {"date": "", "value": None},
                },
                "temperature_mean": {
                    "heighest": {"date": "", "value": None},
                    "lowest": {"date": "", "value": None},
                },
                "humidity_mean": {
                    "heighest": {"date": "", "value": None},
                    "lowest": {"date": "", "value": None},
                },
            }
        """

        ret = {
            "temperature": {
                "heighest": {"date": "", "value": None},
                "lowest": {"date": "", "value": None},
            },
            "humidity": {
                "heighest": {"date": "", "value": None},
                "lowest": {"date": "", "value": None},
            },
            "temperature_mean": {
                "heighest": {"date": "", "value": None},
                "lowest": {"date": "", "value": None},
            },
            "humidity_mean": {
                "heighest": {"date": "", "value": None},
                "lowest": {"date": "", "value": None},
            },
        }

        if month is not None:
            key = f"{year}_{MONTHS[month]}"

            if key not in self._cache or force_reload:
                self._cache[key] = self.read_file(year, month)

            for (date, weather) in self._cache[key].items():
                if (
                    ret["temperature"]["heighest"]["value"] is None
                    or weather.temperature_max is not None
                    and weather.temperature_max
                    > ret["temperature"]["heighest"]["value"]
                ):
                    ret["temperature"]["heighest"]["value"] = weather.temperature_max
                    ret["temperature"]["heighest"]["date"] = date
                if (
                    ret["temperature"]["lowest"]["value"] is None
                    or weather.temperature_min is not None
                    and weather.temperature_min < ret["temperature"]["lowest"]["value"]
                ):
                    ret["temperature"]["lowest"]["value"] = weather.temperature_min
                    ret["temperature"]["lowest"]["date"] = date
                if (
                    ret["humidity"]["heighest"]["value"] is None
                    or weather.humidity_max is not None
                    and weather.humidity_max > ret["humidity"]["heighest"]["value"]
                ):
                    ret["humidity"]["heighest"]["value"] = weather.humidity_max
                    ret["humidity"]["heighest"]["date"] = date
                if (
                    ret["humidity"]["lowest"]["value"] is None
                    or weather.humidity_min is not None
                    and weather.humidity_min < ret["humidity"]["lowest"]["value"]
                ):
                    ret["humidity"]["lowest"]["value"] = weather.humidity_min
                    ret["humidity"]["lowest"]["date"] = date
                if (
                    ret["temperature_mean"]["heighest"]["value"] is None
                    or weather.temperature_mean is not None
                    and weather.temperature_mean
                    > ret["temperature_mean"]["heighest"]["value"]
                ):
                    ret["temperature_mean"]["heighest"][
                        "value"
                    ] = weather.temperature_mean
                    ret["temperature_mean"]["heighest"]["date"] = date
                if (
                    ret["temperature_mean"]["lowest"]["value"] is None
                    or weather.temperature_mean is not None
                    and weather.temperature_mean
                    < ret["temperature_mean"]["lowest"]["value"]
                ):
                    ret["temperature_mean"]["lowest"][
                        "value"
                    ] = weather.temperature_mean
                    ret["temperature_mean"]["lowest"]["date"] = date
                if (
                    ret["humidity_mean"]["heighest"]["value"] is None
                    or weather.humidity_mean is not None
                    and weather.humidity_mean
                    > ret["humidity_mean"]["heighest"]["value"]
                ):
                    ret["humidity_mean"]["heighest"]["value"] = weather.humidity_mean
                    ret["humidity_mean"]["heighest"]["date"] = date
                if (
                    ret["humidity_mean"]["lowest"]["value"] is None
                    or weather.humidity_mean is not None
                    and weather.humidity_mean < ret["humidity_mean"]["lowest"]["value"]
                ):
                    ret["humidity_mean"]["lowest"]["value"] = weather.humidity_mean
                    ret["humidity_mean"]["lowest"]["date"] = date

        else:
            for m in range(len(MONTHS)):
                try:
                    tmp = self.get_extremes(year, m, force_reload)
                    for k, v in tmp.items():
                        if (
                            ret[k]["heighest"]["value"] is None
                            or v["heighest"]["value"] > ret[k]["heighest"]["value"]
                        ):
                            ret[k]["heighest"]["value"] = v["heighest"]["value"]
                            ret[k]["heighest"]["date"] = v["heighest"]["date"]
                        if (
                            ret[k]["lowest"]["value"] is None
                            or v["lowest"]["value"] < ret[k]["lowest"]["value"]
                        ):
                            ret[k]["lowest"]["value"] = v["lowest"]["value"]
                            ret[k]["lowest"]["date"] = v["lowest"]["date"]

                except BaseException:
                    pass
        return ret

    def get_extremes_mean(
        self, year: int, month: int = None, force_reload=False
    ) -> dict[str, dict[str, dict[str, float]]]:
        """Get the mean of the weather for a given year.

        Args:
            year(int): year of the weather
            month(int, optional): month of the weather. Defaults to None.
            force_reload(bool, optional): force reload of the cache. Defaults to False.

        Returns:
            dict[str, dict[str, dict[str, float]]]: Computed Values

            e.g
            {
                "temperature": {
                    "heighest": {"value": 0, "count": 0},
                    "lowest": {"value": 0, "count": 0},
                },
                "humidity": {
                    "heighest": {"value": 0, "count": 0},
                    "lowest": {"value": 0, "count": 0},
                },
                "humidity_mean": {
                    "heighest": {"value": 0, "count": 0},
                    "lowest": {"value": 0, "count": 0},
                },
            }
        """

        ret = {
            "temperature": {
                "heighest": {"value": 0, "count": 0},
                "lowest": {"value": 0, "count": 0},
            },
            "humidity": {
                "heighest": {"value": 0, "count": 0},
                "lowest": {"value": 0, "count": 0},
            },
            "humidity_mean": {
                "heighest": {"value": 0, "count": 0},
                "lowest": {"value": 0, "count": 0},
            },
        }

        if month is not None:
            key = f"{year}_{MONTHS[month]}"

            if key not in self._cache or force_reload:
                self._cache[key] = self.read_file(year, month)

            for _, weather in self._cache[key].items():
                if weather.temperature_max is not None:
                    ret["temperature"]["heighest"]["value"] += weather.temperature_max
                    ret["temperature"]["heighest"]["count"] += 1
                if weather.temperature_min is not None:
                    ret["temperature"]["lowest"]["value"] += weather.temperature_min
                    ret["temperature"]["lowest"]["count"] += 1
                if weather.humidity_mean is not None:
                    ret["humidity_mean"]["lowest"]["value"] += weather.humidity_mean
                    ret["humidity_mean"]["lowest"]["count"] += 1

        else:
            for m in range(len(MONTHS)):
                try:
                    tmp = self.get_extremes_mean(year, m, force_reload)
                    for k, v in tmp.items():
                        ret[k]["heighest"]["value"] += v["heighest"]["value"]
                        ret[k]["heighest"]["count"] += v["heighest"]["count"]
                        ret[k]["lowest"]["value"] += v["lowest"]["value"]
                        ret[k]["lowest"]["count"] += v["lowest"]["count"]
                except BaseException:
                    pass
        return ret

    def get_data(self, year: int, month: int) -> dict[str, Weather]:
        """Get the data of the weather for a given year.

        Args:
            year(int): year of the weather
            month(int): month of the weather

        Returns:
            dict[str, Weather]: key is the date of the weather, value is the weather. 
            Date in format YYYY-MM-DD
        """
        key = f"{year}_{MONTHS[month]}"
        if key not in self._cache:
            self._cache[key] = self.read_file(year, month)
        return self._cache[key]
