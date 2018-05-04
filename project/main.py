#!/usr/bin/env python
# main.py

import signal
import sys, os
import time
import datetime

try:
    file = open("/data/signals.log", 'r')
except IOError:
    file = open("/data/signals.log", 'w')

def signal_term_handler(signal, frame):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    with open("/data/signals.log","a+") as f:
        f.write(st + ' got SIGTERM, cleaning up main.py\n')
    print('got SIGTERM, cleaning up main.py\n', flush=True)
    sys.exit(0)

def signal_int_handler(signal, frame):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    with open("/data/signals.log","a+") as f:
        f.write(st + ' got SIGINT, cleaning up main.py\n')
    print('got SIGINT, cleaning up main.py\n', flush=True)
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_int_handler)

print('my pid is ' + str(os.getpid()))
print("RESIN envvars\n")
for key in os.environ.keys():
    if 'RESIN' in key:
        print(key, os.environ[key])

print('Now I\'m just gonna wait around here for something to happen...')
while True:
    time.sleep(30)
    print("still waiting around...")
