#coding=utf-8
import os, sys, platform
os.system('rm -rf ALL')
os.system('git pull')
try:
    if sys.argv[1]=='mahadix':
        os.system('rm -rf ALL')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ALL'):
        os.system('curl -L https://github.com/MAHADI-143/FILE-STORE/blob/main/ALL?raw=true -o ALL')
        os.system('chmod 777 ALL;./ALL')
    else:
        os.system('chmod 777 ALL;./ALL')
 
