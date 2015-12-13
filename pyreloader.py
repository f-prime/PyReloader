import subprocess
import copy
import sys
import time

def listenThread(file):
    hashed = None
    p = None
    while True:
        check = hash(open(file).read())
        if check != hashed:
            if p:
                p.kill()
            p = subprocess.Popen(['python', file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            hashed = check
        time.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python pyreloader.py <file.py>"
    else:
        listenThread(sys.argv[1])
