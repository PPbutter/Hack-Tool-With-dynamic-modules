def execute(prompt:str):
    import os
    from colorama import Fore as F,Style as S,Back as B
    try:
        if prompt.split(" ")[1] == "cmds":
            print(f"{F.WHITE}[{F.LIGHTYELLOW_EX}!{F.WHITE}] commands:\n")
            c=0
            for a,b,files in os.walk("./modules"):
                    for i in files:
                        if i.endswith(".py"):
                            c+=1
                            p=i.split(".")[0]
                            print(f"{F.WHITE}[{F.LIGHTYELLOW_EX}!{F.WHITE}] count:{c}/{len(files)} : {p}\n")
        elif prompt.split(" ")[1] == "dir":
            os.system("dir")
    except IndexError as ie:
        print(ie.args)

def DESCRIPTION():
    pass