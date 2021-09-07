"""Color Code 사전 정의
"""
from typing import Union


class OutputCellColors:
    """Output Cell의 출력에 표현할 수 있는 색을 정의합니다."""

    FOREGROUND = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bright-black": "\033[90m",
        "bright-red": "\033[91m",
        "bright-green": "\033[92m",
        "bright-yellow": "\033[93m",
        "bright-blue": "\033[94m",
        "bright-magenta": "\033[95m",
        "bright-cyan": "\033[96m",
        "bright-white": "\033[97m",
    }

    BACKGROUND = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
        "bright-black": "\033[90m",
        "bright-red": "\033[91m",
        "bright-green": "\033[92m",
        "bright-yellow": "\033[93m",
        "bright-blue": "\033[94m",
        "bright-magenta": "\033[95m",
        "bright-cyan": "\033[96m",
        "bright-white": "\033[97m",
    }

    F_RESET = "\033[39m"
    B_RESET = "\033[49m"

    def print_all_color_type(self) -> None:
        """8-16 Color Type을 모두 출력합니다."""
        print("Foreground Color Type")
        for name, color in self.FOREGROUND.items():
            print(f"{color}{name}{color}{self.F_RESET}")

        print()

        print("Background Color Type")
        for name, color in self.BACKGROUND.items():
            print(f"{color}{name}{color}{self.B_RESET}")

    def print_all_color_id(self) -> None:
        """256 Color ID를 모두 출력합니다."""
        for i in range(255):
            if i != 0 and i % 10 == 0:
                print()
            colors = f"\033[38;5;{i}m"
            print(f"{colors}{i:3d}{colors}{self.F_RESET}", end=" ")


def colored(text: str, color: Union[str, int]) -> str:
    """글자 색상을 바꿉니다.

    Args:
        text (str): 문자열
        color (Union[str, int]): 사전정의색상 8+8 (black, red, green, yellow, blue, magenta, cyan, white, bright-COLOR(8))

    Returns:
        str: 색상 변경된 문자열
    """
    reset = OutputCellColors.F_RESET

    if isinstance(color, str):
        color = OutputCellColors.FOREGROUND[color.lower()]
        return f"{color}{text}{color}{reset}"

    if isinstance(color, int):
        if color < 0 or color > 255:
            color = OutputCellColors.FOREGROUND["red"]
            print(f"{color}Wrong color id{color}{reset}")
            return text

        color = f"\033[38;5;{color}m"
        return f"{color}{text}{color}{reset}"

    color = OutputCellColors.FOREGROUND["red"]
    print(f"{color}Wrong color type{color}{reset}")
    return text


def bcolored(text: str, color: Union[str, int]) -> str:
    """글자 배경 색상을 바꿉니다.

    Args:
        text (str): 문자열
        color (Union[str, int]): 사전정의색상 8+8 (black, red, green, yellow, blue, magenta, cyan, white, bright-COLOR(8))

    Returns:
        str: 색상 변경된 문자열
    """

    if isinstance(color, str):
        reset = OutputCellColors.B_RESET
        color = OutputCellColors.BACKGROUND[color.lower()]
        return f"{color}{text}{color}{reset}"

    if isinstance(color, int):
        if color < 0 or color > 255:
            reset = OutputCellColors.F_RESET
            color = OutputCellColors.FOREGROUND["red"]
            print(f"{color}Wrong color id{color}{reset}")
            return text

        reset = OutputCellColors.B_RESET
        color = f"\033[48;5;{color}m"
        return f"{color}{text}{color}{reset}"

    reset = OutputCellColors.F_RESET
    color = OutputCellColors.FOREGROUND["red"]
    print(f"{color}Wrong color type{color}{reset}")
    return text
