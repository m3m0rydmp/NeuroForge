import time
import neuroforge
from core import storage
from colorama import just_fix_windows_console, Fore, Style


def run():
    just_fix_windows_console()
    reset = Style.RESET_ALL

    filename = input(f"{Fore.BLUE}Enter filename to export to {Style.BRIGHT}(e.g., \"passwords\" DO NOT INCLUDE the file type): {reset}").strip()
    try:
        with open(filename + '.txt', "w") as f:
            for pw in storage.passwords:
                f.write(pw + "\n")
        print(f"{Style.BRIGHT}[+] Exported {Fore.GREEN}{len(storage.passwords)}{reset} passwords to {Fore.GREEN}{filename}{reset}")
        print(f"Filename: {Fore.GREEN}{filename}.txt{reset}")
        input(f"{Style.BRIGHT}Press Enter to return to the menu...{reset}")
        return neuroforge.show_menu()
    except Exception as e:
        print(f"{Fore.RED}[!] Error exporting: {e}")
        time.sleep(3)
        return neuroforge.show_menu()