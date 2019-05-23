"""
Useless snippet on using ThreadPool, I said it right, its useless this approach
it is here, only for learning, for more meaningful code look at my other thread pool snippets.

IMPORTANT:
Thread pools in any framework are meant to be used to execute short lived tasks,
this is not really important for almost all frameworks EXCEPT for Python.
In Python there is something called GIL which I will not explain here but, it is
the reason why using ThreadPool will not make your application improve its performance most of the times
indeed, it may slow down the app. So you really have to think about using ThreadPool only when needed
and the only situation where you need them is to execute a SHORT LIVED task that you MUST run
in the another thread, if what you are looking for is to free up your process, you have to think
on multiprocessing or the new asyncio module.
"""
import random
import time
from concurrent.futures import ThreadPoolExecutor
import threading

max_sleep_time = 10


def short_lived_task(arg=-1):
    global max_sleep_time
    max_sleep_time -= 2
    print('Sleeping for: %s: %d' % (threading.current_thread().name, arg))
    time.sleep(random.choice(range(1, max_sleep_time)))
    print('Finished for: %s: %d' % (threading.current_thread().name, arg))


# When we use with ThreadPoolExecutor, we will not exit that block
# until all tasks have finished
print("Executing tasks on ThreadPool synchronously")
with ThreadPoolExecutor(max_workers=5) as executor:
    future = executor.submit(short_lived_task, 1)
    future = executor.submit(short_lived_task, 2)
    future = executor.submit(short_lived_task, 3)

print('Finished all tasks')
