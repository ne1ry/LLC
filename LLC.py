#made by ne1ry1881.
import psutil
import os
import ruamel.yaml
import sys
import win32com.client
import time
import fade
import keyboard
from colorama import Fore



shortcut_name = 'ne1ry1881.lnk'
options = '--locale=0'
target_language_code = "0"


entrytext = fade.water("""
       __                 __              __        ______  
      |  \               |  \            |  \      /      \ 
      | $$       ______  | $$            | $$     |  $$$$$$\ 
      | $$      /      \ | $$            | $$     | $$   \$$
      | $$     |  $$$$$$\| $$            | $$     | $$      
      | $$     | $$  | $$| $$            | $$     | $$   __ 
      | $$_____| $$__/ $$| $$_____       | $$_____| $$__/  \ 
      | $$      \$$    $$| $$     \      | $$      \$$    $$
       \$$$$$$$$ \$$$$$$  \$$$$$$$$       \$$$$$$$$ \$$$$$$ 
                                                            
                League Of Legends Language Changer Patch """+Fore.RED+"""13.19"""+Fore.RED+"""

        made by ne1ry1881, contact ne1ry1881 from discord in need.  
        
                                                       
                                                                                                                                                             
""")


options = ["ja_JP: Japanese - 日本語",
           "ko_KR: Korean - 한국어",
           "zh_CN: Chinese - 中文",
           "zh_TW: Taiwanese - 台語",
           "es_ES: Spanish (Spain) - Español (España)",
           "es_MX: Spanish (Mexico) - Español (México)",
           "en_US: English (USA) - English (USA)",
           "en_GB: English (Great Britain) - English (Great Britain)",
           "en_AU: English (Australia) - English (Australia)",
           "fr_FR: French - Français",
           "de_DE: German - Deutsch",
           "it_IT: Italian - Italiano",
           "pl_PL: Polish - Polski",
           "ro_RO: Romanian - Română",
           "el_GR: Greek - Ελληνικά",
           "pt_BR: Portuguese - Português",
           "hu_HU: Hungarian - Magyar",
           "ru_RU: Russian - Русский",
           "tr_TR: Turkish - Türkçe",
           "cs_CZ: Czech - Čeština"]

selected_option = 0

def print_options():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(entrytext)
    for i, option in enumerate(options):
        if i == selected_option:
            print(Fore.LIGHTMAGENTA_EX + "[X]" + Fore.GREEN + f" >>> {option}")
        else:
            print(Fore.LIGHTRED_EX + "[X]" + Fore.BLUE + f"  {option}")

print_options()

while True:
    key = keyboard.read_event(suppress=True).name
    time.sleep(0.1)

    if key in ['up', 'w']:
        selected_option = (selected_option - 1) % len(options)
    elif key in ['down', 's']:

        selected_option = (selected_option + 1) % len(options)
    elif key == 'enter':
        break

    print_options()

target_language_code = options[selected_option].split(":")[0]
print(Fore.BLACK+"[-]\n"+Fore.BLACK+"[-]\n" + Fore.LIGHTMAGENTA_EX + "[X]" + Fore.BLUE +
      " Changing Your Language to:  >>> " + Fore.GREEN + f" {options[selected_option]} {target_language_code}" + Fore.BLUE + "  <<<")
dil = {options[selected_option]}
options = f'--locale={target_language_code}'

wewewewe = input(Fore.BLACK+"[-]"  + "\n"+Fore.BLUE+"[?]" + Fore.GREEN + f"               Press Enter To Start The Process")

def change_lol_language(installation_path, language_code):
    try:
        config_path = os.path.join(installation_path, "Config", "LeagueClientSettings.yaml")
        print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" Found League Of Legends Folder Path ")
        time.sleep(0.1)
    except:
        print(Fore.RED + "[-]" + Fore.GREEN + f" League Of Legends Folder Path is Not Founded")
        print(Fore.RED + "[-]" + Fore.GREEN + f" This Window Will Automatically Close after 10 Seconds.")
        time.sleep(10)
        sys.exit()

    yaml = ruamel.yaml.YAML()
    with open(config_path, "r") as config_file:
        config_data = yaml.load(config_file)

    config_data["install"]["globals"]["locale"] = language_code

    try: 
        with open(config_path, "w") as config_file: 
            yaml.dump(config_data, config_file)
            print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" Language Code is Written to .yaml File. ")
            time.sleep(0.1)
    except:
        print(Fore.RED + "[-]" + Fore.GREEN + f" Unexpected Error Happened While Writing the Language code to .yaml File, Please Check Folder Path")
        print(Fore.RED + "[-]" + Fore.GREEN + f" This Window Will Automatically Close after 10 Seconds.")
        time.sleep(10)
        sys.exit()




def change_shortcut_options(shortcut_path, new_options):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    
    shortcut.Targetpath += new_options
    try:
        shortcut.save()
        print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" Shortcut is Succesfully modified Desktop.")
        time.sleep(0.1)
    except:
        print(Fore.RED + "[-]" + Fore.GREEN + f" Unexpected Error Happened While Modifying the Shortcut")
        print(Fore.RED + "[-]" + Fore.GREEN + f" This Window Will Automatically Close after 10 Seconds.")
        time.sleep(10)
        sys.exit()


def create_desktop_shortcut(target_path, shortcut_name):
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    try:
        shortcut.save()
        print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" Shortcut is Succesfully modified Desktop.")
        time.sleep(0.05)
    except:
        print(Fore.RED + "[-]" + Fore.GREEN + f" Unexpected Error Happened While Saving the Shortcut")
        print(Fore.RED + "[-]" + Fore.GREEN + f" This Window Will Automatically Close after 10 Seconds.")
        time.sleep(10)
        sys.exit()

lol_installation_path = r"C:\Riot Games\League of Legends"


change_lol_language(lol_installation_path, target_language_code)

print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" Changed Language To: {dil}")
lolgame_installation_path = r"C:\Riot Games\League of Legends"
target_exe_path = os.path.join(lolgame_installation_path, 'LeagueClient.exe')

create_desktop_shortcut(target_exe_path, "ne1ry1881"),


import subprocess


def run_shortcut_with_options(shortcut_path, options):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" Desktop Path: {desktop_path} ")
    shortcut_path = os.path.join(desktop_path, shortcut_name)
    print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" Shortcut Path: {shortcut_path} ")
    command = f'start "" "{shortcut_path}" {options}'
    subprocess.run(command, shell=True)

try:
    run_shortcut_with_options(shortcut_name, options)
    print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" Changed Language Succesfully.")
    time.sleep(0.2)
    print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" League of Legends is Launching... Wait few seconds ")
except:
    print(Fore.RED + "[-]" + Fore.GREEN + f" Unexpected Error Happened Running Leauge of Legends")
    print(Fore.RED + "[-]" + Fore.GREEN + f" This Window Will Automatically Close after 10 Seconds.")
    time.sleep(10)
    sys.exit()
while True:
    def is_process_running(process_name):
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                return True
        return False

    process_name = 'RiotClientServices.exe'

    if is_process_running(process_name):
        print(Fore.LIGHTMAGENTA_EX + "\r[+] " + Fore.GREEN + "You Can Launch Your Game Now! Thanks for Using this Tool.")
        print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.GREEN + f" This Window Will Automatically Close after 10 Seconds.")
        print(Fore.LIGHTMAGENTA_EX + "[+]" + Fore.RESET + f"                   -- n e 1 r y 1 8 8 1 -- ")
        time.sleep(10)
        time.sleep(10)
        sys.exit()
    else:
        def loading_effect():
            chars = ['-','\\','|','/']
            for _ in range(10):  
                for char in chars:
                    print(Fore.LIGHTMAGENTA_EX + "\r[+] " + Fore.GREEN +f"Waiting For The Riot Client to Respond...    {char}" , end='', flush=True)
                    time.sleep(0.1)
        loading_effect()