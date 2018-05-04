import time
import sys
import signal

try:
    file = open("/data/signals.txt", 'r')
except IOError:
    file = open("/data/signals.txt", 'w')

def wf():
    with open('/data/signals.txt', 'a+') as f:
        print("closed all resources\n", flush=True)
        f.write("Closed resources!")
        f.flush()

        

def quit_gracefully(*args):
    wf()
    sys.exit(-1)

signal.signal(signal.SIGINT, quit_gracefully)
signal.signal(signal.SIGTERM, quit_gracefully)

while True:
    print("I am alive!")
    time.sleep(30)