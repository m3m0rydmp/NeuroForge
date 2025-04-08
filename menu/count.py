from core import storage
from colorama import just_fix_windows_console, Fore, Style


def run():
    just_fix_windows_console()
    reset = Style.RESET_ALL

    print(f"{Fore.GREEN}{Style.BRIGHT}[+] Total stored passwords: {len(storage.passwords)}{reset}")