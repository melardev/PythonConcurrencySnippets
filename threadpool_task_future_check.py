from concurrent.futures import ThreadPoolExecutor
from time import sleep


def square_task(number):
    print('Task execution started')
    sleep(2)
    print('Task execution finished')
    return number ** 2


executor = ThreadPoolExecutor(5)
future = executor.submit(square_task, 2)
print('Has task finished? %s' % future.done())
sleep(3)
print('Has task finished? %s' % future.done())

# result() is blocking, so if you call it, make sure the task is complete: done() == true
# unless you are ok with blocking the current thread waiting the task to finish
print(future.result())
