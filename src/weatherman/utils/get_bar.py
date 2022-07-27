from termcolor import colored


def get_bar(value: int, max_value: int, bar_width=100, char="#", color=None) -> str:
    """Returns a bar with a given value and max value.

    Args:
        value (int): value of the bar
        max_value (int): max value of the bar
        bar_width (int, optional): width of the bar. Defaults to 100.
        char (str, optional): to use for the bar. Defaults to "#".
        color (str, optional): color of the bar. Defaults to None.

    Returns:
        str: A colored bar.
    """

    return char * int(value / max_value * bar_width) if color is None else colored(
        char * int(value / max_value * bar_width), color
    )
