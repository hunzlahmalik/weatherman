from weatherman.constants import MONTHS
from weatherman.weatherman import WeatherMan
from weatherman.utils import draw_bar
import sys


def main():
    if sys.argv[1] == "--help":
        print("Usage: weatherman <folder path> <switch> <year/month>")
        print("Switch:")
        print("\t--help: show this help")
        print("\t--extremes | -e : show the extremes of the weather")
        print("\t--averages | -a : show the extreams of mean of the weather")
        print("\t--chart | -c : make a bar chart of the weather")
        sys.exit(0)

    filepath = sys.argv[1]

    w = WeatherMan(filepath)

    for i in range(2, len(sys.argv), 2):
        if sys.argv[i] == "--extremes" or sys.argv[i] == "-e":
            date = (sys.argv[i + 1]).split("/")
            isMonth = len(date) > 1
            res = w.get_extremes(int(date[0]), int(
                date[1]) - 1 if isMonth else None)
            print(
                "Highest: {}C on {} {}\nLowest: {}C on {} {}\nHumidity: {}% on {} {}".format(
                    res["temperature"]["heighest"]["value"],
                    MONTHS[
                        int(res["temperature"]["heighest"]
                            ["date"].split("-")[1]) - 1
                    ],
                    res["temperature"]["heighest"]["date"].split("-")[2],
                    res["temperature"]["lowest"]["value"],
                    MONTHS[int(res["temperature"]["lowest"]
                               ["date"].split("-")[1]) - 1],
                    res["temperature"]["lowest"]["date"].split("-")[2],
                    res["humidity"]["heighest"]["value"],
                    MONTHS[int(res["humidity"]["heighest"]
                               ["date"].split("-")[1]) - 1],
                    res["humidity"]["heighest"]["date"].split("-")[2],
                )
            )

        elif sys.argv[i] == "--averages" or sys.argv[i] == "-a":
            date = (sys.argv[i + 1]).split("/")
            isMonth = len(date) > 1
            res = w.get_extremes_mean(
                int(date[0]), int(date[1]) - 1 if isMonth else None
            )
            print(
                "Highest Temperature: {}C\nLowest Temperature: {}C\nAverage Mean Humidity: {}%".format(
                    res["temperature"]["heighest"]["value"]
                    / res["temperature"]["heighest"]["count"],
                    res["temperature"]["lowest"]["value"]
                    / res["temperature"]["lowest"]["count"],
                    res["humidity_mean"]["lowest"]["value"]
                    / res["humidity_mean"]["lowest"]["count"],
                )
            )

        elif sys.argv[i] == "--chart" or sys.argv[i] == "-c":
            date = (sys.argv[i + 1]).split("/")
            isMonth = len(date) > 1
            if not isMonth:
                print("Error: month is not specified")
                sys.exit(1)

            res = w.get_data(int(date[0]), int(date[1]))

            print(f"{MONTHS[int(date[1])-1]} {date[0]}")
            for date, weather in res.items():
                if weather.temperature_max is None or weather.temperature_min is None:
                    continue
                print(
                    "{} {}{} {}C - {}C".format(
                        date.split("-")[2],
                        draw_bar(
                            weather.temperature_min,
                            weather.temperature_min + weather.temperature_max,
                            50,
                            color="blue",
                            print_bar=False,
                        ),
                        draw_bar(
                            weather.temperature_max,
                            weather.temperature_min + weather.temperature_max,
                            50,
                            color="red",
                            print_bar=False,
                        ),
                        weather.temperature_min,
                        weather.temperature_max,
                    )
                )

        else:
            print("Unknown switch: " + sys.argv[i])
            sys.exit(1)
        print()

    sys.exit()


if __name__ == "__main__":
    main()
