from threading import Thread
from Queue import Queue

class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, result_list, args, kwargs = self.queue.get()
            try:
                res = func(*args, **kwargs)
                result_list.append((func, res, args, kwargs),)
            except Exception, e:
                print e
            finally:
                self.queue.task_done()

class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads, qsize=None):
        self.num_threads = num_threads
        self.queue = Queue(qsize)

    def start(self):
        for _ in range(self.num_threads): 
            Worker(self.queue)

    def addTask(self, func, result_list, *args, **kargs):
        """Add a task to the queue"""
        self.queue.put((func, result_list, args, kargs))

    def wait(self):
        """Wait for completion of all the tasks in the queue"""
        self.queue.join()
