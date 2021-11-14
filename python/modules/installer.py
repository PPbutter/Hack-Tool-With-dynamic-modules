def execute(prompt:str):
    import pip
    if len(prompt.split("-p ")) >= 2:
        if prompt.startswith("installer install"):
            pip.main(["install",prompt.split("-p ")[1]])
            print("\n")

def install(package:str):
    import pip
    pip.main(["install",package])

def DESCRIPTION():
    from colorama import Fore as F
    return f"i install stuff so u don\'t have to. :){F.CYAN}\n{F.WHITE}Usage: installer install -p <package name>{F.CYAN}\n{F.WHITE}Example: installer install requests"