#!/usr/bin/python

'''Example of multithreading python.
  
  Prints start, end, then wake up.
  We create a thread using the threading library, then pass it the target kwarg
  takeANap (not takeANap(), because we want to pass the function itself as the
  argument and not call the function and pass the return value from it).

  The start() method creates the new thread and starts executing the target
  function in the new thread. 

  wake up is printed after end because the target function takeANap is being run
  a separate thread and executing simultaneously, waiting for 5 seconds before
  printing wake up. 

  Python programs won't terminate until all threads have terminated. This means
  the program is still running while the second thread is waiting, and only when
  it is done will the program exit.
'''

import threading
import time


print 'start of the program <=== thread 1'

def takeANap():
  time.sleep(5)
  print 'Wake up! <=== thread 2'

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print 'end of the program <=== thread 1'

