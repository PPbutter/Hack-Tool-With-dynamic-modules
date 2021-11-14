def execute(prompt:str):
    from colorama import Fore as F,Style as S
    msg = prompt.split("-m ")[1]
    print(f"{S.BRIGHT}[{F.YELLOW}!{F.WHITE}] {msg}\n")


def DESCRIPTION():
    return "prints what you want when you want"