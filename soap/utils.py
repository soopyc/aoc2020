import colorama


colorama.init(autoreset=True)


def warn(value, text="WARN", end='\n\n', *args, **kwargs):
    print(
            f"{colorama.Back.YELLOW}"
            f"{colorama.Fore.BLACK}{colorama.Style.BRIGHT} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end,
            *args, **kwargs
    )


def info(value, text="INFO", end='\n\n', *args, **kwargs):
    print(
            f"{colorama.Back.BLUE}"
            f"{colorama.Fore.WHITE}{colorama.Style.BRIGHT} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end,
            *args, **kwargs
    )


def error(value, text="ERROR", end='\n\n', *args, **kwargs):
    print(
            f"{colorama.Back.RED}"
            f"{colorama.Fore.WHITE}{colorama.Style.BRIGHT} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end,
            *args, **kwargs
    )


def debug(value, text="DEBUG", end='\n', *args, **kwargs):
    print(
            f"{colorama.Back.LIGHTBLACK_EX}"
            f"{colorama.Fore.WHITE}{colorama.Style.BRIGHT} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end,
            *args, **kwargs
    )


def success(value, text="SUCCESS", end='\n\n', *args, **kwargs):
    print(
            f"{colorama.Back.GREEN}"
            f"{colorama.Fore.WHITE}{colorama.Style.BRIGHT} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end,
            *args, **kwargs
    )


def question(value, text="INPUT", *args, **kwargs):
    a = input(f"{colorama.Back.CYAN}{colorama.Fore.WHITE}"
              f"{colorama.Style.BRIGHT} {text} {colorama.Style.RESET_ALL}"
              f" {value} ",
              *args, **kwargs)
    print()
    return a


