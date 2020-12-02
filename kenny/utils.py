import colorama


colorama.init(autoreset=True)


def warn(value, text="WARN", end='\n\n', *args, **kwargs):
    print(
            f"{colorama.Back.LIGHTYELLOW_EX}"
            f"{colorama.Fore.BLACK} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end
            *args, **kwargs
    )


def info(value, text="INFO", end='\n\n', *args, **kwargs):
    print(
            f"{colorama.Back.LIGHTBLUE_EX}"
            f"{colorama.Fore.BLACK} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end
            *args, **kwargs
    )


def error(value, text="ERROR", end='\n\n', *args, **kwargs):
    print(
            f"{colorama.Back.LIGHTRED_EX}"
            f"{colorama.Fore.BLACK} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end
            *args, **kwargs
    )


def debug(value, text="DEBUG", end='\n\n', *args, **kwargs):
    print(
            f"{colorama.Back.LIGHTBLACK_EX}"
            f"{colorama.Fore.WHITE} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end
            *args, **kwargs
    )


def success(value, text="SUCCESS", end='\n\n', *args, **kwargs):
    print(
            f"{colorama.Back.LIGHTGREEN_EX}"
            f"{colorama.Fore.WHITE} {text} "
            f"{colorama.Style.RESET_ALL} "
            f"{value}", end=end
            *args, **kwargs
    )


def question(value, text="INPUT", *args, **kwargs):
    a = input(f"{colorama.Back.LIGHTCYAN_EX}{colorama.Fore.BLACK}"
              f" {text} {colorama.Style.RESET_ALL} {value} ",
              *args, **kwargs)
    print()
    return a


