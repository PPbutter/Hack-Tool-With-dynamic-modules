import os
import requests 
import terminaltables
import time
from datetime import datetime#,terminaltables
from colorama import Fore as F,Style as S,Back as B 



ipApi = "http://ip-api.com/json/"

commands = ['ip','exec','exit','help','req']

commandsDesc = [f'get data on the targets IP addr{F.CYAN}\n{F.WHITE}Usage: ip <Target IP>{F.CYAN}\n{F.WHITE}example: ip 24.60.200.10',f'[exec]ute a command to the terminal{F.CYAN}\n{F.WHITE}Usage: exec <system command>{F.CYAN}\n{F.WHITE}example: exec echo hi','exits the program dummy','shows you this help screen',f'request data from a website (simalar to a web crawler){F.CYAN}\n{F.WHITE}Usage: req <get> <website destination>{F.CYAN}\n{F.WHITE}example: req get www.google.com']

commandsAndDesc = ""

newLines = f"{F.CYAN}"

for i in range(0,len(commands)):
    newLines = newLines + "\n\n\n"
    commandsAndDesc = commandsAndDesc.__add__(f"{F.CYAN}{F.WHITE}{commands[i]} : {commandsDesc[i]}{F.CYAN}\n\n\n\n\n")

newLines = newLines + f"{F.CYAN}{F.WHITE}COMMANDS{F.CYAN}"


helpTable = terminaltables.DoubleTable([[f"{F.WHITE}{newLines}",commandsAndDesc]]).table


DISCLAIMER = f"""{F.WHITE}[{F.LIGHTYELLOW_EX}!{F.WHITE}] this tool is inteded for educational uses only
under any misuse of this product with malitious intent in any circum stance only YOU will be held accountable"""

print(DISCLAIMER)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

print(f"{F.CYAN}")

print(helpTable,f"\n{F.WHITE}")


def resultss(data):
    ipApi = "http://ip-api.com/json/"
    red = F.RED

    a = F.LIGHTGREEN_EX+S.BRIGHT+"[$]"
    b = F.CYAN+S.BRIGHT+"[$]"
    print (a, "[Target]:", data['query'])
    print(red+"<--------------->"+red)
    print (b, "[ISP]:", data['isp'])
    print(red+"<--------------->"+red)
    print (a, "[Organisation]:", data['org'])
    print(red+"<--------------->"+red)
    print (b, "[City]:", data['city'])
    print(red+"<--------------->"+red)
    print (a, "[Region]:", data['region'])
    print(red+"<--------------->"+red)
    print (b, "[Longitude]:", data['lon'])
    print(red+"<--------------->"+red)
    print (a, "[Latitude]:", data['lat'])
    print(red+"<--------------->"+red)
    print (b, "[Time zone]:", data['timezone'])
    print(red+"<--------------->"+red)
    print (a, "[Zip code]:", data['zip'])

def crawl(method:str,destination:str):

    methods = ['get','post']
    if method.replace(" ","") == methods[0]:
        #req = None
        try:
            req = requests.get("https://"+destination)
            return req
        except:
            req = requests.get("http://"+destination)
            return req

while True:
    try:
        currentTime = datetime.now().strftime("%H:%M:%S")
        prompt = input(f"{S.BRIGHT}{F.WHITE}[{F.GREEN}{currentTime}{F.WHITE}] {F.LIGHTCYAN_EX}hackr{F.GREEN} ➮{F.RESET}{F.LIGHTBLUE_EX} ")
        print(F.RESET)
        if prompt.startswith(commands[0]):
            try:
                m = prompt.split(" ")
                if len(m) == 2:
                    if m[1] == "":
                        raise BaseException
                if len(m) >= 3:
                    raise IndexError
                if m[1] == "-":
                    req = requests.get(f"http://ip-api.com/json/").json()
                else:
                    req = requests.get(f"http://ip-api.com/json/{m[1]}").json()

                print(f"{F.LIGHTRED_EX}<--------S-T-A-T-S-------->\n")
                resultss(req)
                print("")
            except IndexError:
                if len(m) >= 3:
                    print(f"{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err sufficient arguments: there where {len(m)} too many arguments supplied out of 2\n")
                else:
                    print(f"{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err sufficient arguments: there where only {len(m)} argument supplied out of 2\n")
            except BaseException:
                print(f"{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err Please supply at leat 1 argument\n")
            

        elif prompt.startswith(commands[1]):
            z=""
            r=0
            p = prompt.split(" ")
            for a in p:
                if r != 0:
                    #pass
                    z = z.__add__(a+" ")
                r+=1
            #print(z)
            os.system(z)
            print(F.RESET,S.NORMAL)
        elif commands[2] == prompt:
            exit(f"\n{F.WHITE}[{F.LIGHTYELLOW_EX}!{F.WHITE}] bye-bye {F.LIGHTCYAN_EX}:){F.WHITE}\n")
        elif commands[3] == prompt:
            print(f"{F.CYAN}\n")
            print(helpTable,f"\n{F.WHITE}")
        elif prompt.startswith("req"):
            q = prompt.split("req")
            qq = prompt.split("get")
            dat=crawl(prompt.split(" ")[1],qq[1].replace(" ",""))
            print(f"\n{S.BRIGHT}[{F.GREEN}${F.WHITE}] URL:{F.LIGHTGREEN_EX} {dat.url} {F.WHITE}")
            print(f"\n{S.BRIGHT}[{F.LIGHTCYAN_EX}${F.WHITE}] STATUS CODE:{F.LIGHTCYAN_EX} {dat.status_code} {dat.reason} {F.WHITE}")
            if len(dat.text) > 2000:
                km = input(f"\n{S.BRIGHT}[{F.BLUE}?{F.WHITE}] hmm. . . it appears the data from the website is around ({len(dat.text)}) characters would you like to save it to a file insted (Y/N)?: ")
                if km.lower() == "y":
                    pp = input("what would you like to save the file as (with extention): ")
                    fa = open(pp,"w")
                    fa.write(dat.text)
                    fa.close()
        else:
            if prompt != "":
                print(f"\n{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err command not found: {F.LIGHTYELLOW_EX}{prompt}{F.WHITE}\n")
    except KeyboardInterrupt as keyInterupt:
        print(f"\n\n{F.WHITE}{S.BRIGHT}[{F.YELLOW}!{F.WHITE}] remember if your trying to exit type the command exit :)\n{S.NORMAL}")