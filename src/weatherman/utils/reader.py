from dataclasses import dataclass
from weatherman.weather import Weather


def reader(filepath: str) -> dict[str, Weather]:
    """
    Reads a weather file and returns a dict of @Weather objects.
    @example:
    >>> reader('weather.txt')
    {'2018-1-1' : Weather(year=2018, month=1, day=1, temperature_max=10.0, temperature_mean=5.0,...), ...}
    """

    # checking sperator, currently supported ',', ';' and '\t'
    ext = filepath.split(".")[-1]
    sep = "," if ext == "csv" or ext == "txt" else ";" if ext == "tsv" else "\t"
    # reading file
    with open(filepath, "r") as f:
        lines = f.readlines()
    # removing header
    lines = lines[1:]
    # remobing empty lines
    lines = [line for line in lines if line.strip()]
    # creating dict of Weather objects
    weathers = {}
    for line in lines:
        line = line.strip()
        line = line.split(sep)
        date_split = line[0].split("-")
        weathers[line[0]] = Weather(
            year=int(date_split[0]),
            month=int(date_split[1]),
            day=int(date_split[2]),
            temperature_max=float(line[1]) if line[1] != "" else None,
            temperature_mean=float(line[2]) if line[2] != "" else None,
            temperature_min=float(line[3]) if line[3] != "" else None,
            dew=float(line[4]) if line[4] != "" else None,
            dew_mean=float(line[5]) if line[5] != "" else None,
            dew_min=float(line[6]) if line[6] != "" else None,
            humidity_max=float(line[7]) if line[7] != "" else None,
            humidity_mean=float(line[8]) if line[8] != "" else None,
            humidity_min=float(line[9]) if line[9] != "" else None,
            pressure_max=float(line[10]) if line[10] != "" else None,
            pressure_mean=float(line[11]) if line[11] != "" else None,
            pressure_min=float(line[12]) if line[12] != "" else None,
            visibility_max=float(line[13]) if line[13] != "" else None,
            visibility_mean=float(line[14]) if line[14] != "" else None,
            visibility_min=float(line[15]) if line[15] != "" else None,
            windspeed_max=float(line[16]) if line[16] != "" else None,
            windspeed_mean=float(line[17]) if line[17] != "" else None,
            gustspeed_max=float(line[18]) if line[18] != "" else None,
            precipitation=float(line[19]) if line[19] != "" else None,
            cloudcover=float(line[20]) if line[20] != "" else None,
            events=line[21] if line[21] != "" else None,
            wind_director=float(line[22]) if line[22] != "" else None,
        )
    return weathers
