import sys
import time
from subprocess import call

status = False

def main():
    while(True):
        servo(status)

def servo(status):
    if status == "start":
        main()
    if status == False:
            call (["echo 2=70 > /dev/servoblaster"], shell=True)
            print "kiri"
            status = True
            time.sleep(2)
    if status == True:
            call (["echo 2=130 > /dev/servoblaster"], shell=True)
            print "kanan"
            status = False
            time.sleep(2)
    if status == "Stop":
            #call (["echo 2=130 > /dev/servoblaster"], shell=True)
            print "stop"
            exit()

if __name__ == "__main__":
    main()
