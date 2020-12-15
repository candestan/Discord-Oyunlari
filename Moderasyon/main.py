import os
import argparse
from lysep import LysepBot
from lib.settings import TOKEN, COMMAND_PREFIX, BOT_VERSION, THEME_COLOR_DEFAULT
from colorama import Fore, init
import shutil
columns, rows = shutil.get_terminal_size(fallback=(80, 24))
init(autoreset=True)
def main():
    print(Fore.CYAN + "WELCOME TO LYSEP BOT FRAMEWORK".center(columns, " "))
    print(Fore.YELLOW + "BY LYSEP CORP".center(columns, " "))
    parser = argparse.ArgumentParser("LYSEP Discord Bot")
    parser.add_argument("--debug","-D",action="store_true")
    parser.add_argument("--release","-R",action="store_true")
    parser.add_argument("--custom-key","-CK",type=str)
    print(Fore.LIGHTGREEN_EX + "[!] Starting with release mode...")
    OyunBotu = LysepBot(TOKEN, COMMAND_PREFIX, BOT_VERSION, THEME_COLOR_DEFAULT)
    OyunBotu.Start()
if __name__ == "__main__":
    main()