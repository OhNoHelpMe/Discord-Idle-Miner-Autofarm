import requests
import time
import random
import colorama
from colorama import Fore, Style

def banner():
    colorama.init()
    print(f"""
    {Fore.GREEN}
  _____    _ _        __  __ _                                 _         __                     
 |_   _|  | | |      |  \/  (_)                     /\        | |       / _|                    
   | |  __| | | ___  | \  / |_ _ __   ___ _ __     /  \  _   _| |_ ___ | |_ __ _ _ __ _ __ ___  
   | | / _` | |/ _ \ | |\/| | | '_ \ / _ \ '__|   / /\ \| | | | __/ _ \|  _/ _` | '__| '_ ` _ \ 
  _| || (_| | |  __/ | |  | | | | | |  __/ |     / ____ \ |_| | || (_) | || (_| | |  | | | | | |
 |_____\__,_|_|\___| |_|  |_|_|_| |_|\___|_|    /_/    \_\__,_|\__\___/|_| \__,_|_|  |_| |_| |_|

                                                                            Made by V0RT3X#2796
                                                                                {Style.RESET_ALL}
    """)

def start():
    # ------------------------------------------------------
    commands = [";s", ";up b h", ";up p a", ";f", ";h", ";o a", ";claimall", ";prestige", ";rb"]
    # ------------------------------------------------------

    # ------------------------------------------------------
    # ;s         -> sell
    # ;up b h    -> upgrade pickaxe half
    # ;up p a    -> upgrade backpack all
    # ;f         -> fish
    # ;h         -> hunt
    # ;o a       -> open all crates
    # ;claimall  -> claim all
    # ;rb        -> rebirth
    # ------------------------------------------------------
    banner()
    # ------------------------------------------------------
    token = input("[?] Discord Token: ")
    channel_id = input("[?] Channel_ID: ")
    print("")
    # ------------------------------------------------------

    # ------------------------------------------------------
    while True:
        for i in range(len(commands)):
            header = {'authorization': token}
            payload = {'content': commands[i]}
            print("[+] Executing ", commands[i])
            r = requests.post( "https://discord.com/api/v9/channels/" + channel_id + "/messages", data=payload, headers=header )
            randInt = random.randint(5,7)
            print("[+] Waiting ", randInt, "s ...")
            time.sleep(randInt)
    print("Autofarm stopped!")
    # ------------------------------------------------------

if __name__ == '__main__':
    start()
