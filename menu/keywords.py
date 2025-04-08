import time
import neuroforge
from core import storage
from colorama import just_fix_windows_console, Fore, Style

def run():
    just_fix_windows_console()
    reset = Style.RESET_ALL

    keywords_display = ', '.join(storage.keywords) if storage.keywords else "None"
    print(f"{Fore.BLUE}\nCurrent Keywords: {Fore.GREEN}{Style.BRIGHT}{keywords_display}{reset}")


    user_input = input(f"{Fore.BLUE}Enter new keywords (comma-separated). ENTER for nothing: {reset}").strip()
    if user_input:
        new_keywords = [kw.strip() for kw in user_input.split(",")]
        storage.keywords.extend(new_keywords)
        storage.keywords = list(set(storage.keywords))

        storage.save_all()

        print(f"{Fore.GREEN}{Style.BRIGHT}Successfully added keywords!{reset}")
        time.sleep(2)
        return neuroforge.show_menu()
    else:
        print(f"{Fore.RED}{Style.BRIGHT}No keywords entered. No changes made.{reset}")
        time.sleep(2)
        return neuroforge.show_menu()