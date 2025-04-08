import neuroforge
import time
from core import storage
from colorama import just_fix_windows_console, Fore, Style


def run():
    just_fix_windows_console()
    reset = Style.RESET_ALL

    print(f"\n{Style.BRIGHT}{Fore.BLUE}[1] Delete generated passwords")
    print(f"[2] Delete current keywords{reset}")
    choice = input(f"{Style.BRIGHT}Select an option (1 or 2): ").strip()

    if choice == '1':
        confirm = input(f"{Fore.BLUE}\nAre you sure you want to delete all generated {Style.BRIGHT}PASSWORDS? (y/n): {reset}").strip().lower()
        if confirm.startswith('y'):

            if len(storage.passwords) == 0:
                print(f"{Fore.BLUE}\n[!] There are currently no passwords to delete.{reset}")
                time.sleep(2)
                return neuroforge.show_menu()
            else:
                storage.passwords.clear()
                print(f"{Fore.GREEN}\n[+] All generated passwords have been cleared.{reset}")
                time.sleep(2)
                return neuroforge.show_menu()
        else: 
            print(f"{Fore.RED}\n[!] Operation cancelled.{reset}")
            time.sleep(2)
            return neuroforge.show_menu()

    elif choice == '2':
        confirm = input(f"{Fore.BLUE}\nAre you sure you want to delete all {Style.BRIGHT}KEYWORDS? (y/n): {reset}").strip().lower()
        if confirm.startswith('y'):

            if len(storage.keywords) == 0:
                print(f"{Fore.BLUE}\n[!] There are currently no keywords to delete.{reset}")
                time.sleep(2)
                return neuroforge.show_menu()
            else:
                storage.keywords.clear()
                print(f"{Fore.GREEN}\n[+] All keywords have been cleared.{reset}")
                time.sleep(2)
                return neuroforge.show_menu()
        else:
            print(f"{Fore.RED}\n[!] Operation cancelled.{reset}")
            time.sleep(2)
            return neuroforge.show_menu()

    else:
        print(f"{Fore.RED}\n[!] Invalid option{reset}")
        time.sleep(2)
        return neuroforge.show_menu()