#!/usr/bin/env python3

from colorama import init, Fore, Style
init(autoreset=True)

class TerminalTools(object):
    def __init__(self):
        pass

    @staticmethod
    def Red(txt):
        print(Fore.RED + txt)
            
    @staticmethod
    def Yellow(txt):
        print(Fore.YELLOW + txt)
    
    @staticmethod
    def Green(txt):
        print(Fore.GREEN + txt)