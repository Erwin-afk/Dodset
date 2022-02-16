import os
import wget
import sys
import time
from colorama import Fore, Style
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
init()

y = ["y","Y","yes","YES"]
n = ["n","N","no","NO"]

title="""
█▀▄ █▀█ █▀▄ █▀ █▀▀ ▀█▀
█▄▀ █▄█ █▄▀ ▄█ ██▄ ░█░ v0.7 \n
--- Author: Erwin ---\n"""
print(title)


text = (f"[{Fore.YELLOW}-{Style.RESET_ALL}] Launching 'MesterMC.exe'")
n_text = (f"[{Fore.YELLOW}-{Style.RESET_ALL}] Closing {Fore.LIGHTBLUE_EX}Dodset{Style.RESET_ALL}...")

link = "https://rubugvkrwjee.mestermc.hu/3TtRL64MJ7yV1YQ/BrutalTelepito116.exe"

input(f"Press '{Fore.CYAN}enter{Style.RESET_ALL}' to start")

def main():
    try:
        wget.download(link,"MesterMC.exe")
        print(f"[{Fore.GREEN}v{Style.RESET_ALL}] Succes!")
        os.system("cls")

        y_n = input("Would you like to launch 'MesterMC.exe'? Y/N ")


        if y_n in y:
            os.system("cls")
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.0001)
            os.system("MesterMC.exe")


        elif y_n in n:
            os.system("cls")
            for char in n_text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.0001)
            time.sleep(2)
            pass
        

        else:
            os.system("cls")
            pass

    except:
        print(f"[{Fore.RED}x{Style.RESET_ALL}] Failed.")
        try:
            os.remove("MesterMC.exe")
        except:
            time.sleep(3)
        pass
main()
