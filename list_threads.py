import threading

for thread in threading.enumerate():
    print(thread.name)
