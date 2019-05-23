"""
This is a Thread pool implementation, obviously you should not be using this code
Python provides a very well written thread pool implementation way better than this one
This snippet is only meant to show how thread pools may be working behind the scenes in a very generic
way. But definitely, real world implementations are more complex, they take care of synchronization and
low level details which I don't here.
"""
import threading
from queue import Queue

sentinel = None


class TaskRunner(threading.Thread):

    def __init__(self, owner, queue, id):
        self._owner = owner
        threading.Thread.__init__(self, name=self._owner.get_name() + "_" + str(id))
        self.daemon = True
        self._queue = queue

    def run(self):
        while self._owner.running:
            value = self._queue.get()
            # sentinel is my indicator of exiting
            if value is sentinel:
                break
            func, args, kwargs = value

            if func is not None:
                try:
                    func(*args, **kwargs)
                except Exception as error:
                    self._owner.on_error(error)
                self._queue.task_done()


class ThreadPool:

    def __init__(self, name, queue_size, thread_count, error_callback):
        self._destroy = False
        self._name = name
        self._error_callback = error_callback
        self._queue = Queue(queue_size)
        self._thread_count = thread_count
        self._threads = []
        self.running = False

    def get_name(self):
        return self._name

    def start(self):
        self.running = True
        for i in range(self._thread_count):
            task_runner = TaskRunner(self, self._queue, i)
            self._threads.append(task_runner)
            task_runner.start()

    def submit_async(self, func, *args, **kwargs):
        if not self._destroy:
            self._queue.put([func, args, kwargs])

    def stop(self):
        self._running = False
        for i in range(len(self._threads)):
            self._queue.put(sentinel)

    def join(self):
        for thread in self._threads:
            thread.join()

    def on_error(self, err):
        self._error_callback(err)


def on_error(err):
    pass


def task(*args, **kwargs):
    print('Executed on %s, args: %s, kwargs: %s' % (threading.current_thread().name, args, kwargs))


thread_pool = ThreadPool('Snippet', 20, 4, on_error)
thread_pool.start()

count = 0

for i in range(0, 5):
    thread_pool.submit_async(task, count, count + 1, param1=count, param2=count + 2)
    count += 1
    thread_pool.submit_async(task, count, count + 1, param1=count, param2=count + 2)
    count += 1

thread_pool.stop()
thread_pool.join()
