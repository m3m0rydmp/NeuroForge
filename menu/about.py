from colorama import just_fix_windows_console, Fore, Style
import neuroforge

def run():
    just_fix_windows_console()
    reset = Style.RESET_ALL

    print(f"""{Fore.BLUE}

███╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
████╗  ██║██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║   ██║█████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
██║ ╚████║███████╗╚██████╔╝██║  ██║╚██████╔╝██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
          
          {reset}{Style.BRIGHT}
------------------------------------------------------------------------------------------------
This program is a password generator and manager. It allows you to generate random passwords,
based on the keywords you provide, and store them securely. You can also export your passwords to a
file.

The program is inspired when a person does OSINT and needs to generate passwords based on the
keywords of the target. It is not intended for malicious use, and the author is not responsible 
for any misuse of this program.


Written by: {Fore.GREEN}{Style.BRIGHT}m3m0rydmp{reset}
    """)
    input("Press Enter to return to the menu...")
    return neuroforge.show_menu()