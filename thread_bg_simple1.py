import threading
import time


def func_thread():
    time.sleep(3)
    print("this thread is called %s)" % threading.current_thread().name)
    print("the main thread is called %s" % threading.main_thread().name)


child = threading.Thread(target=func_thread, daemon=True)
child.start()

