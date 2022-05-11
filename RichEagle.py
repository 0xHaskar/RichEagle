import os
#=============
print('''
▒█▀▀█ ▀ █▀▀ █  █ ▒█▀▀▀ █▀▀█ █▀▀▀ █   █▀▀
▒█▄▄▀ █ █   █▀▀█ ▒█▀▀▀ █▄▄█ █ ▀█ █   █▀▀
▒█░▒█ ▀ ▀▀▀ ▀  ▀ ▒█▄▄▄ ▀  ▀ ▀▀▀▀ ▀▀▀ ▀▀▀
''')
print("Developed by 0xHaskar")
#============
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
#=============================
print(color.BOLD + color.BLUE + "========================================")
print("1. Social Engineering    | ❌")
print("2. OSINT                 | ✅")
#=======================================
select = input(color.BOLD + color.GREEN + "Select: ")
print('\033[39m') # delete color
#========================================
if select == "1":
    dir = os.getcwd()
    os.chdir(dir + "/modules/social_engineering/")
    os.system("clear")
    os.system("python3 SE_start.py")

if select == "2":
    dir = os.getcwd()
    os.chdir(dir + "/modules/osint/")
    os.system("clear")
    os.system("python3 osint_start.py")
