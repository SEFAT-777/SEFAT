#coding=utf-8
import os, sys, platform
os.system('rm -rf MAHADIIX')
os.system('git pull')
try:
    if sys.argv[1]=='mahadix':
        os.system('rm -rf MAHADIIX')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('MAHADIIX'):
        os.system('curl -L https://github.com/MAHADI-XD/TEST/blob/main/MAHADIIX?raw=true -o MAHADIIX')
        os.system('chmod 777 MAHADIIX;./MAHADIIX')
    else:
        os.system('chmod 777 MAHADIIX;./MAHADIIX')
 
