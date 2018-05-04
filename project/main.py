import time
import sys
import signal

try:
    file = open("/data/signals.txt", 'r')
except IOError:
    file = open("/data/signals.txt", 'w')

def wf():
    with open('/data/signals.txt', 'w') as f:
        f.write("Closed resources!")
        print("closed all resources", flush=True)
        f.flush()

def quit_gracefully(*args):
    wf()
    sys.exit(-1)

signal.signal(signal.SIGINT, quit_gracefully)
signal.signal(signal.SIGTERM, quit_gracefully)

while True:
    print("I am alive!")
    time.sleep(30)