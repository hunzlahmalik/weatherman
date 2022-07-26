from weatherman.constants import CONSOLE_COLORS as COLORS


def draw_bar(
    value: int,
    max_value: int,
    bar_width=100,
    char="#",
    color="green",
    print_bar=True,
    print_end="\n",
    print_sep="",
) -> str:
    """
    Draw a bar with a given value and max value.
    @param value: value of the bar
    @param max_value: max value of the bar
    @param bar_width: width of the barÍ
    @param char: character to use for the bar
    @param color: color of the bar
    @param print_bar: print the bar or not
    @example:
    >>> draw_bar(10, 50, 10, 'red')
    >>> draw_bar(10, 50, 10, 'red', False)
    """
    bar_length = int(value / max_value * bar_width)
    bar = char * bar_length
    bar = COLORS[color] + bar
    if print_bar:
        print(bar, end=print_end, sep=print_sep)
        print(COLORS["reset"], end="")
    return bar + COLORS["reset"]
