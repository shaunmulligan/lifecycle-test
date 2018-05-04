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
    print('got SIGTERM, cleaning up main.py\n', flush=True)
    with open("/data/signals.log","a+") as f:
        f.write('got SIGTERM, cleaning up main.py\n')
        f.flush()
    # sys.exit(0)

def signal_int_handler(signal, frame):
    print('got SIGINT, cleaning up main.py\n', flush=True)
    with open("/data/signals.log","a+") as f:
        f.write('got SIGINT, cleaning up main.py\n')
        f.flush()
    # sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_int_handler)

print('my pid is ' + str(os.getpid()))
# print("RESIN envvars\n")
# for key in os.environ.keys():
#     if 'RESIN' in key:
#         print(key, os.environ[key])

print('Now I\'m just gonna wait around here for something to happen...')
while True:
    time.sleep(30)
    print("still waiting around...")
