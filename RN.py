import os
from platform import architecture
if architecture()[0]=='64bit':os.system('git pull;chmod +x AM;./AM')

elif architecture()[0]=='32bit':os.system('git pull;chmod +x AM;./AM')

else:exit('\033[1;31m\n Sorry unknown device not support ')
