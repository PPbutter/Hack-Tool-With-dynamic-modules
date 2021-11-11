def execute(prompt:str):
    from colorama import Fore as F, Style as S
    while True:
        try:
            import requests
            from colorama import Fore as F,Style as S,Back as B 
            break
        except ModuleNotFoundError as iE:
            import time
            import installer as inst
            inst.install([iE.name])
            time.sleep(5)

    def reqq(method:str,destination:str):
        if method == 'get':
            try:
                req = requests.get("https://"+destination)
                return req
            except:
                req = requests.get("http://"+destination)
                return req

    def handle(dat):
            print(f"\n{S.BRIGHT}[{F.GREEN}${F.WHITE}] URL:{F.LIGHTGREEN_EX} {dat.url} {F.WHITE}")
            print(f"\n{S.BRIGHT}[{F.LIGHTCYAN_EX}${F.WHITE}] STATUS CODE:{F.LIGHTCYAN_EX} {dat.status_code} {dat.reason} {F.WHITE}")
            if len(dat.text) > 2000:
                km = input(f"\n{S.BRIGHT}[{F.BLUE}?{F.WHITE}] hmm. . . it appears the data from the website is around ({len(dat.text)}) characters would you like to save it to a file insted (Y/N)?: ")
                if km.lower() == "y":
                    pp = input("what would you like to save the file as (with extention): ")
                    fa = open(pp,"w")
                    fa.write(dat.text)
                    fa.close()
    
    try:
        m = prompt.split(" ")
        print(m,len(m))
        if len(m) == 3:
            re = reqq(m[1],m[2])
            handle(re)
        elif m[1] == "":
            raise BaseException
        elif len(m) >= 3:
            raise IndexError

        
    except IndexError:
        if len(m) >= 3:
            print(f"\n{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err sufficient arguments: there where {len(m)} too many arguments supplied out of 2\n")
        else:
            print(f"\n{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err sufficient arguments: there where only {len(m)} argument supplied out of 3\n")            #prompt,prompt.split(" ")[1]
    
    except BaseException:
        print(f"{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err Please supply at least 1 argument\n")


def DESCRIPTION(): 
    from colorama import Fore as F,Style as S
    return f'request data from a website (simalar to a web crawler){F.CYAN}\n{F.WHITE}Usage: req <get> <website destination>{F.CYAN}\n{F.WHITE}example: req get www.google.com'