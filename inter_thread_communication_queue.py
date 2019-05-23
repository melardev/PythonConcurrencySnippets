import sys
import threading
import queue

# sentinel object is anything that indicates a stop on the task
# you could use None as a sentinel, indeed IMO that is what is used the most of the times
import time

sentinel = object()


def order_work(q):
    for i in range(0, 10):
        q.put(i)
        time.sleep(1)
    q.put(sentinel)


def do_work(q):
    while True:
        value = q.get()
        if value is sentinel:
            sys.stdout.write("\nexiting\n")
            return
        sys.stdout.write(str(value))


q = queue.Queue()

t1 = threading.Thread(target=do_work, args=(q,))
t2 = threading.Thread(target=order_work, args=(q,))
t1.start()
t2.start()
