import threading


def background_thread(args):
    print(threading.current_thread().name + " got " + str(args))


# When we pass one single arg to the thread, we must specify that parentheses is not a wrapper
# but a tuple indicator, because arg is expecting an iterator, so either use [i] for list
# or for a tuple use (i,) to indicate it is a tuple, (i) would mean just an integer wrapped with parentheses
for i in range(10):
    thread = threading.Thread(target=background_thread, args=(i,))
    thread.start()
