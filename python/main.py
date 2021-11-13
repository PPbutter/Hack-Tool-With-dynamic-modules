while True:
    try:
        import os
        import random
        import importlib
        import mrkool as mk
        import terminaltables
        from datetime import datetime
        from colorama import Fore as F,Style as S,Back as B 
        break
    except ModuleNotFoundError as iE:
        import time
        import installer as inst
        inst.install([iE.name])
        time.sleep(5)


class collect:
    c=0
    def import_(dest:str):
        MOD = importlib.import_module(dest)
        shiz = ['__builtins__','__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
        
        mods = []

        for b in dir(MOD):
            if b not in shiz:
                if b == "DESCRIPTION":
                    name = dest.split(".")[1]
                    mods.append(MOD.__getattribute__(b))
                elif b == "execute":
                    name = dest.split(".")[1]
                    mods.append(MOD.__getattribute__(b))
        
        return [MOD,mods,name]


modules = []

modFunctions = []

modNames = []

modDic = {}

for a,b,file in os.walk("./modules"):
    for i in file:
        if i.endswith(".py"):
            i = "modules." + i.split(".")[0]
            p = collect.import_(dest=i)
            modules.append(p[0])
            modFunctions.append(p[1])
            modNames.append(p[2])


c=0
cc = 0
for i in modNames:
    modDic[i] = {'module':modules[c],'desc':[],'func':[]}
    for ii in range(0,len(modFunctions)):
        cc=0
        for iii in modFunctions[ii]:
            if cc == 0:
                if ii == c:
                    modDic[i]['desc'].append(iii)
            if cc == 1:
                if ii == c:
                    modDic[i]['func'].append(iii)
            cc+=1
    c+=1


commands = []

commandsAndDesc = ""

commandsDesc = []

for i in modDic:
    commands.append(i)

for i in commands:
    commandsDesc.append(modDic[i]['desc'][0]())


#print(modDic)

newLines = f"{F.CYAN}"

commandsAndDesc = commandsAndDesc.__add__(f"{F.CYAN}{F.WHITE}help : gets help on a specific command{F.CYAN}\n{F.WHITE}Usage: help <Command>{F.CYAN}\n{F.WHITE}Example: help {modNames[random.randint(0,len(modNames)-1)]}{F.CYAN}\n\n\n\n\n")


for i in range(0,len(commands)):
    newLines = newLines + "\n\n\n"
    commandsAndDesc = commandsAndDesc.__add__(f"{F.CYAN}{F.WHITE}{commands[i]} : {commandsDesc[i]}{F.CYAN}\n\n\n\n\n")

newLines = newLines + f"{F.CYAN}{F.WHITE}COMMANDS{F.CYAN}"

helpTable = terminaltables.DoubleTable([[f"{F.WHITE}{newLines}",commandsAndDesc]]).table


while True:
    try:
        currentTime = datetime.now().strftime("%H:%M:%S")
        prompt = f"{S.BRIGHT}{F.WHITE}[{F.GREEN}{currentTime}{F.WHITE}] {F.LIGHTCYAN_EX}hackr{F.GREEN} ➮{F.RESET}{F.LIGHTBLUE_EX} "
        inpu = input(prompt)
        print(f"{F.WHITE}")
        
        if inpu == "help":
            print(f"{F.CYAN}")
            print(helpTable)

        
        elif inpu == "exit":
            exit(f"\n{F.WHITE}[{F.LIGHTYELLOW_EX}!{F.WHITE}] bye bye {F.LIGHTCYAN_EX}:){F.WHITE}\n")
        
        elif inpu != "help":

            for a in modDic:
                if inpu.startswith(a):
                    if len(inpu.split(" ")) >= 2:
                        mk.executer2000.run(modDic[a]['module'],modDic[a]['func'][0](inpu))

                elif len(inpu.split(" ")) >= 2:
                    if inpu.split(" ")[1] == a:
                        if inpu.startswith("help "):
                            if len(inpu.split(" ")) == 2:
                                pp = mk.executer2000.run(modDic[a]['module'],modDic[a]['desc'][0]())
                                pa = 0
                                for i in f"{pp}".split(f"{F.CYAN}\n{F.WHITE}"):
                                    if pa == 0:
                                        print(f"{S.BRIGHT}[{F.LIGHTYELLOW_EX}!{F.WHITE}] Description: {i}\n")
                                    else:
                                        print(f"{S.BRIGHT}[{F.LIGHTYELLOW_EX}!{F.WHITE}] {i}\n")
                                    pa+=1
                            #print(f"\n{S.BRIGHT}[{F.LIGHTYELLOW_EX}!{F.WHITE}] {a} DESCRIPTION: {pp}\n")
                else:
                    print(f"{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err command not found: {F.LIGHTYELLOW_EX}{inpu}{F.WHITE}\n")
                    break
        #else:
        #    print(f"{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err command not found: {F.LIGHTYELLOW_EX}{inpu}{F.WHITE}\n\n")
    
    except KeyboardInterrupt as keyInterupt:
        print(f"\n\n{F.WHITE}{S.BRIGHT}[{F.YELLOW}!{F.WHITE}] remember if your trying to exit type the command exit :)\n{S.NORMAL}")            