def execute(prompt:str):
    from colorama import Fore as F, Style as S
    import os
    z= ""
    r= 0
    p = prompt.split(" ")
    for a in p:
        if r != 0:
            #pass
            z = z.__add__(a+" ")
        r+=1
    #print(z)
    os.system(z)
    print(F.RESET,S.NORMAL)

def DESCRIPTION():
    from colorama import Fore as F,Style as S
    return f'[exec]ute a command to the terminal{F.CYAN}\n{F.WHITE}Usage: exec <system command>{F.CYAN}\n{F.WHITE}example: exec echo hi'