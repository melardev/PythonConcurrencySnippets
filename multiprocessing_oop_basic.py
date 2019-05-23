import multiprocessing
import random


class Process(multiprocessing.Process):

    def run(self):
        print('Running in process %s' % self.name)
        return


if __name__ == '__main__':
    processes = []
    for i in range(random.randint(4, 8)):
        process = Process()
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
