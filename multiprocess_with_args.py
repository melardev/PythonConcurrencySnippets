import multiprocessing


def worker(num):
    print('Worker %s, argument: %s' % (multiprocessing.current_process().name, num))
    return


if __name__ == '__main__':
    processes = []
    for i in range(5):
        # the same as for threading, we have to pass an iterable as argument
        # so if we pass a single arg, make sure to explicitly tell the interpreter
        # it is a tuple and not an int enclosed with parentheses, or just use a list: [i]
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
