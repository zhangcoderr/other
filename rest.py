import time
import os

while(True):
    print('restart!')
    os.system('notepad')
    minute=0
    while(minute<15):
        print('minute: '+str(minute))
        time.sleep(60)
        minute=minute+1
    os.system('notepad')



