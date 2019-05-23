import threading
import time


def func_thread():
    time.sleep(3)
    print("this thread is called %s" % threading.current_thread().name)
    print("the main thread is called %s" % threading.main_thread().name)


other_thread = threading.Thread(target=func_thread, name="Background Thread")

print('Is other_thread daemon? %s' % other_thread.isDaemon())
other_thread.start()
print("main thread is daemon? : %s" % threading.current_thread().isDaemon())
# Notice the script does not exit here, because the other thread is running AND because it is not Daemon
# if other_thread was daemon, once the script is finished, the other_thread will be killed
# try this if you don't believe me:
# other_thread = threading.Thread(target=func_thread, name="Background Thread", daemon=True)
# or this
# other_thread.setDaemon(False)
