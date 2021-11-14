def execute(prompt:str):
    while True:
        try:
            import requests
            from colorama import Fore as F,Style as S
            break
        except ModuleNotFoundError as mnfe:
            import time
            import modules.installer as inst
            inst.install(mnfe.name)
            time.sleep(5)
    ipApi = "http://ip-api.com/json/"
    data = requests.get(ipApi)
    red = F.RED

    if prompt.startswith("ip"):
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
            data = req
            print("")
        except IndexError:
            if len(m) >= 3:
                print(f"\n{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err sufficient arguments: there where {len(m)} too many arguments supplied out of 2\n")
            else:
                print(f"\n{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err sufficient arguments: there where only {len(m)} argument supplied out of 2\n")
        except BaseException:
            print(f"{F.WHITE}{S.BRIGHT}[{F.LIGHTRED_EX}X{F.WHITE}] Err Please supply at least 1 argument\n")
        except:
            pass
    try:
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
        print('')
    except:
        pass

def DESCRIPTION():
    from colorama import Fore as F,Style as S 
    return f'get data on the targets IP addr{F.CYAN}\n{F.WHITE}Usage: ip <Target IP> | ip < - > {F.CYAN}\n{F.WHITE}example: ip 24.60.200.10 | ip -'