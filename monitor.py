# this will poll to check if Sublime is opened
# since it doesn't support editor exit events
#
# https://github.com/SublimeText/Issues/issues/582

import os
import time
import sys
import subprocess

pid  = int(sys.argv[1])
port = sys.argv[2]

while True:
    time.sleep(1)

    try:
        os.kill(pid,0)
    except OSError, e:
        subprocess.Popen(['livedown', 'stop', '--port', port])
        sys.exit()
