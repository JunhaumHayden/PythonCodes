from threading import Thread
from time import sleep
import time

class MyThread(Thread):
    def __init__(self, name, sleep_time):
        self.sleep_time = sleep_time
        super().__init__(name=name)
    # Override the run method to define the thread's behavior
    def run(self):
        print(self.name + ' started...\n', end=' ')
        sleep(self.sleep_time)
        print(self.name + " finished after " + str(self.sleep_time) + " seconds.\n", end=' ')


def main():
    threads01 = []
    loops = 10
    time_worker = time.time()
    for i in range(loops):
        # Create threads in a loop with args
        threads01.append(MyThread("Thread-" + str(i+1), i+3))
        # start threads
        threads01[i].start()
        if threads01[i].is_alive():
            print(threads01[i].name + " is alive.\n", end=' ')

    # Wait for threads to finish
    for i in range(loops):
        # Join threads to ensure they complete before exiting
        threads01[i].join()
        print(threads01[i].name + " has finished.\n", end=' ')
    print('Time taken: ', time.time() - time_worker)

if __name__ == '__main__':
    main()