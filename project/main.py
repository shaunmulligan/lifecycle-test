#!/usr/bin/env python
# main.py

import signal
import sys, os
import time

def receive_signal(signum, stack):
    if signum in [1,2,3,15]:
        with open("/data/signals.log", "a+") as f:
            f.write('Caught signal %s, cleaning up and exiting main.py.' %(str(signum)))
            f.flush()
            os.fsync(f.fileno())
        print 'Caught signal %s, cleaning up and exiting main.py.' %(str(signum))
        sys.exit(0)
    else:
        print 'Caught signal %s, ignoring.' %(str(signum))

uncatchable = ['SIG_DFL','SIGSTOP','SIGKILL']
for i in [x for x in dir(signal) if x.startswith("SIG")]:
    if not i in uncatchable:
        signum = getattr(signal,i)
        signal.signal(signum,receive_signal)

print 'my pid is ' + str(os.getpid())
print "RESIN envvars\n"
for key in os.environ.keys():
    if 'RESIN' in key:
        print key, os.environ[key]

print 'Now I\'m just gonna wait around here for something to happen...'
while True:
    time.sleep(30)
    print "still waiting around..."
