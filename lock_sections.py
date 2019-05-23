import threading
import time
import random

lock = threading.Lock()


def background_thread(num):
    print(threading.current_thread().name + " begin heavy work")
    # using with statements makes it easy, the lock is release()'d automatically after with statement
    with lock:
        # lock.acquire()
        # make any changes you need
        time.sleep(random.randint(1, 3))
        print(threading.current_thread().name + " end")
    # lock.release()


for i in range(10):
    thread = threading.Thread(target=background_thread, args=(i,))
    thread.start()
