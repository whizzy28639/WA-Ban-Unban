import os
import time
import subprocess
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def run_bash_script():
    try:
        if os.path.exists('request.sh'):
            subprocess.Popen(['bash', 'request.sh'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print(Fore.YELLOW + "Note: request.sh file not found, continuing without it.")
    except Exception as e:
        pass

def show_about():
    print(Fore.CYAN + "\nAbout Page:")
    print(Fore.YELLOW + "Made By 𝐁𝐈𝐆 𝐖𝐇𝐈𝐙𝐙𝐘 2025/11/25")
    print(Fore.GREEN + "Ban tool v1.1f-request-python3")
    print(Fore.GREEN + """
▇◤▔▔▔▔▔▔▔◥▇ Whatsapp attack number
▇▏◥▇◣┊◢▇◤▕▇
▇▏▃▆▅▎▅▆▃▕▇ ban or unban ..
▇▏╱▔▕▎▔▔╲▕▇
▇◣◣▃▅▎▅▃◢◢▇ tool is illegal ..
▇▇◣◥▅▅▅◤◢▇▇
▇▇▇◣╲▇╱◢▇▇▇ We are not responsible for your use of this tool.

    """)
    input("\nPress Enter to go back to the main menu...")
    clear_screen()

def run_whatsapp_tools():
    try:
        os.system('python whatsapp_tool.py')
    except FileNotFoundError:
        print(Fore.RED + "Error: whatsapp_tools.py file not found!")

def animate_text(text, delay=0.05):
    for char in text:
        print(Fore.BLUE + char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    run_bash_script()

    while True:
        clear_screen()
        print(Fore.GREEN + f"""
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__________¶¶¶____¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
________¶¶¶__¶¶__¶¶_¶¶¶¶_¶¶¶¶___¶¶¶¶¶¶_¶¶¶¶¶
______¶¶¶__¶¶¶__¶¶__¶¶¶¶_¶¶¶¶___¶¶¶¶¶¶__¶¶¶¶¶¶
____¶¶¶___¶¶¶___¶¶_¶¶¶¶¶_¶¶¶¶____¶¶¶¶¶¶___¶¶¶¶¶
___¶¶___¶¶¶¶¶__¶¶__¶¶¶¶¶_¶¶¶¶____¶¶¶¶¶¶¶____¶¶¶¶¶
_¶¶____¶¶¶¶¶___¶¶__¶¶¶¶¶_¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶
¶¶¶¶¶_____¶¶__¶¶__¶¶¶¶¶¶_¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶____¶¶¶__¶¶¶¶¶¶_¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
___¶¶¶___¶¶¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_____¶¶__¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶
_______¶¶_¶¶¶_¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶
________¶¶__¶¶_¶¶__¶¶¶¶¶_¶¶¶______¶¶¶¶___¶¶¶
__________¶¶_¶¶_¶¶__¶¶¶¶_¶¶¶_____¶¶¶¶__¶¶¶
___________¶¶_¶¶_¶¶_¶¶¶¶__¶¶____¶¶¶¶__¶¶¶
_____________¶¶_¶_¶¶_¶¶¶__¶¶___¶¶¶¶_¶¶¶
_______________¶_¶_¶¶_¶¶__¶¶__¶¶¶¶_¶¶¶
________________¶¶__¶__¶__¶¶__¶¶¶¶¶¶
__________________¶__¶____¶¶_¶¶¶¶¶¶
___________________¶¶_¶___¶¶¶¶¶¶¶
_____________________¶¶¶__¶¶¶¶¶¶
______________________¶¶¶_¶¶¶¶
________________________¶¶¶¶¶
__________________________¶
    """)

        print(Fore.GREEN + "1. 𝐒𝐓𝐀𝐑𝐓")
        print(Fore.GREEN + "2. 𝐀𝐁𝐎𝐔𝐓")
        print(Fore.GREEN + "3. 𝐄𝐗𝐈𝐓")

        choice = input("\n𝐒𝐄𝐋𝐄𝐂𝐓 𝐀𝐍 𝐎𝐏𝐓𝐈𝐎𝐍 : ")

        if choice == '1':
            run_whatsapp_tools()
        elif choice == '2':
            show_about()
        elif choice == '3':
            print(Fore.RED + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")

if __name__ == "__main__":
    main()
