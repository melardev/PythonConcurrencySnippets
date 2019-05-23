import multiprocessing
import time


def worker1():
    name = multiprocessing.current_process().name
    print('%s: Running' % name)
    time.sleep(1)
    print('%s: Done' % name)


def worker2():
    name = multiprocessing.current_process().name
    print('%s: Running' % name)
    time.sleep(3)
    print('%s: Done' % name)


def worker3(arg):
    name = multiprocessing.current_process().name
    print('%s: Running with arg %s' % (name, arg))
    time.sleep(3)
    print('%s: Done' % name)


if __name__ == '__main__':
    # if a name is not assigned, it will be given an automatic name
    worker_1 = multiprocessing.Process(target=worker1)
    worker_2 = multiprocessing.Process(name='worker 1', target=worker1)
    worker_3 = multiprocessing.Process(name='worker 2', target=worker2)
    worker_4 = multiprocessing.Process(name='worker 3', target=worker3, args=['Multiprocessing Snippet'])

    worker_1.start()
    worker_2.start()
    worker_3.start()
    worker_4.start()

    worker_1.join()
    worker_2.join()
    worker_3.join()
    worker_4.join()
