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
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
        # removing header
        lines = lines[1:]
        # removing empty lines
        lines = [line for line in lines if line.strip()]
        # creating dict of Weather objects
        weathers = {}
        for line in lines:
            line = line.strip()
            line = line.split(sep)
            weathers[line[0]] = Weather(
                temperature_max=float(line[1]) if line[1] != "" else None,
                temperature_mean=float(line[2]) if line[2] != "" else None,
                temperature_min=float(line[3]) if line[3] != "" else None,
                humidity_max=float(line[7]) if line[7] != "" else None,
                humidity_mean=float(line[8]) if line[8] != "" else None,
                humidity_min=float(line[9]) if line[9] != "" else None,
            )
        return weathers
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return {}
