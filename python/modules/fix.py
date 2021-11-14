def execute(prompt:str):
    from colorama import Fore as F,Style as S
    try:
        filePath = prompt.split("-fp ")[1].split(" ")[0].split(" ")[0]
    except IndexError:
        print(f"{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] please supply a file path.\nkinda like this: fix -fp <path to ur file> | file.txt")
    try:
        replaceWhat = prompt.split("-rw ")[1].split(" ")[0]
    except IndexError:
        print(f"{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] please supply a character you want to replace.\nkinda like this: fix -rw <path to ur file> | file.txt")
    try:
        replaceWith = prompt.split("-rW ")[1].split(" ")[0]
    except IndexError:
            print(f"{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] please supply a character you want to replace with the one you selected to replace.\nkinda like this: fix -rW <path to ur file> | file.txt")

    file = open(filePath,"r")
    ree = file.read()
    ree = ree.replace(replaceWhat,replaceWith)
    file.close()
    b=filePath.split(".")
    newFile = open(f"{b[0]}-fixed.{b[1]}","w")
    newFile.write(ree)
    newFile.close()

def DESCRIPTION():
    from colorama import Fore as F,Style as S,Back as B
    return f"{F.WHITE}it replaces certain things in a file{F.CYAN}\n{F.WHITE}Usage: fix -fp <path to file name> -rw <replace what> -rW <replace with>{F.CYAN}\n{F.WHITE}Example: fix -fp ./example.txt -rw hi -rW bye"