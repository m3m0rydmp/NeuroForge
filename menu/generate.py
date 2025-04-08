import time
from core import generator, storage
from colorama import just_fix_windows_console, Fore, Style
from neuroforge import show_menu


def run():
    global reset

    just_fix_windows_console()
    reset = Style.RESET_ALL
    while True:
        try:
            if len(storage.keywords) == 0:
                print(f"{Fore.RED}[!] No keywords{reset} are stored yet. This will result in a random password.")
                user_input = input(f"{Style.BRIGHT}Do you want to continue? (y/n): {reset}").strip().lower()
                if not user_input.startswith("y"):
                    print(f"{Fore.RED}[!] Exiting...{reset}")
                    time.sleep(1)
                    return show_menu()
                else:
                    print(f"{Fore.YELLOW}[!] Continuing...{reset}")

            length = int(input(f"{Fore.BLUE}Password length: "))
            count = int(input("How many passwords to generate? "))
            result = generator.generate(length, count)

            
            storage.passwords.extend(result)
            storage.save_all()

            print(f"{reset}{Fore.GREEN}{Style.BRIGHT}\n[+] Generated Passwords:{reset}")
            for pw in result:
                print(Style.BRIGHT + pw)
            
            input(f"\n{Fore.BLUE}Press Enter to return to the menu...{reset}")
            return show_menu()
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{reset}")
            time.sleep(2)
            return show_menu()
