import signal
import sys, os
from colorama import just_fix_windows_console, Fore, Style
from core import storage
from menu import generate, keywords, count, export, delete, about, menu_quit

# Colorama Fix for Windows
just_fix_windows_console()

def show_menu():
    global reset

    reset = Style.RESET_ALL

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Fore.BLUE}
        
███╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
████╗  ██║██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║   ██║█████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
██║ ╚████║███████╗╚██████╔╝██║  ██║╚██████╔╝██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                                                      
    {reset}{Fore.GREEN}{Style.BRIGHT}
            
       ========================= MAIN MENU =========================
       * *                                                       * *      
       * *                1.) Generate Password                  * *
       * *                2.) Input Keywords                     * *
       * *                3.) Count Total Passwords              * *
       * *                4.) Export Passwords                   * *
       * *                5.) Delete Passwords/Keywords          * *
       * *                6.) About the Program                  * *
       * *                7.) Exit Program                       * *
       * *                                                       * *
       * *                                                       * *
       ==============================================================

{reset}""")
    
def signal_handler(sig, frame):
    print("\n[!] Exiting...")
    storage.save_all()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    storage.load_all()

    menu_map = {
        '1': generate.run,
        '2': keywords.run,
        '3': count.run,
        '4': export.run,
        '5': delete.run,
        '6': about.run,
        '7': menu_quit.run
    }
    
    show_menu()
    while True:
        choice = input(f"{Style.BRIGHT}SELECT an option: ").strip()
        action = menu_map.get(choice)
        if action:
            action()
        else:
            print(f"{Fore.RED}[!] Invalid option. Please try again.{reset}")
            

if __name__ == "__main__":
    main()
