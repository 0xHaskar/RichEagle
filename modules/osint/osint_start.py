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
print(color.BOLD + color.BLUE + "1.  | ✅")
#==================================
select = input(color.BOLD + color.GREEN + "Select: ")
print('\033[39m') # delete color
#========================================

