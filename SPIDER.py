import os,time,platform
bit = platform.architecture()[0]
if bit=='64bit':
    import RN
else:
    print('\033[1;31m[×] Sorry your Device 32 bit Not Support')
 
