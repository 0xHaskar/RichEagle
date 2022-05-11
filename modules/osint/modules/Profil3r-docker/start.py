import os
#===============
print('''
▒█▀▀█ ▀ █▀▀ █  █ ▒█▀▀▀ █▀▀█ █▀▀▀ █   █▀▀
▒█▄▄▀ █ █   █▀▀█ ▒█▀▀▀ █▄▄█ █ ▀█ █   █▀▀
▒█░▒█ ▀ ▀▀▀ ▀  ▀ ▒█▄▄▄ ▀  ▀ ▀▀▀▀ ▀▀▀ ▀▀▀
''')
#=======================================
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
#==================================
print(color.BOLD + color.BLUE + "========================================")
print(color.BOLD + color.BLUE + "𝙊𝙎𝙄𝙉𝙏")
print(color.BOLD + color.BLUE + "========================================")
print(color.BOLD + color.BLUE + "1. start profil3r        | ✅")
print(color.BOLD + color.BLUE + "2. profil3r -help        | ✅")
print(color.BOLD + color.BLUE + "3. sudo install profil3r | ✅")
#==================================
select = input(color.BOLD + color.GREEN + "Select: ")
print('\033[39m') # delete color
#========================================
if select == "1":
    profil3r = input( color.BOLD + color.GREEN + "User name: ")
    os.system("python3 profil3r.py -p " + profil3r)

if select == "2":
    os.system("clear")
    print('''
    Version 1.3.11 - Developped by Rog3rSm1th
    You can buy me a coffee at : https://www.buymeacoffee.com/givocefo
    github: https://github.com/MrNonoss/Profil3r-docker

    usage: profil3r.py [-h] -p PROFILE [PROFILE ...]
    ''')
    os.system("python3 start.py")

if select == "3":
    os.system("clear")
    os.system("sudo python3 setup.py install")
