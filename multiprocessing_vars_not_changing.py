"""
This snippet proves to you that processes have their own context, so the Python Objects are different
if you change something in one process, it is not changed in the other process, keep that in mind!!
"""
import multiprocessing
import random
import time


class Test:
    some_value = 3


test = Test()


class Process(multiprocessing.Process):
    def __init__(self):
        super(Process, self).__init__()
        self.my_value = 5

    def run(self):
        print('%s: test.some_value is %s' % (self.name, test.some_value))
        test.some_value = 10
        self.my_value = 25
        return


if __name__ == '__main__':
    processes = []
    for i in range(random.randint(3, 5)):
        process = Process()
        processes.append(process)
        process.start()
        time.sleep(1)

    for process in processes:
        process.join()
        # this will be unchanged, why? because it has been changed in other process, not in this one!!
        print('process: %s, process.my_value is %s' % (process.name, test.some_value))

# this will be unchanged, why? because it has been changed in other process, not in this one!!
print('test.some_value is %s' % test.some_value)
