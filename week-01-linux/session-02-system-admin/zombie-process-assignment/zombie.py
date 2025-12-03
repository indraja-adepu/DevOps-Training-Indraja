import os
import time

pid = os.fork()

if pid == 0:
    # Child exits immediately → becomes zombie
    print("Child process exiting..")
    os._exit(0)
else:
    # Parent sleeps and does NOT clean child
    time.sleep(1000)
    print("This is the parent process. Sleeping...")
    
