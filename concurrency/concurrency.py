from threading import Thread
import time

def read_name():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

def calculate():
    #print("Calculating...", end=' ')
    [(x**2) for x in range(1000000)]
    #print("Done...", end=' ')

def calculate_power(pow):
    #print("Calculating power %d" %  pow, end=' ')
    [(x**pow) for x in range(1000000)]
    #print("Done...%d" % pow, end=' ')

def main():
    time_to_worker01 = time.time()
    #read_name()
    calculate()
    print('\nTime Sequential taken                                 :', time.time() - time_to_worker01)

    # Create a thread for reading name
    time_to_worker = time.time()
    #thread01 = Thread(target=read_name) #inicialize thread
    thread02 = Thread(target=calculate)    #inicialize thread
    #thread01.start()                                       #start thread
    thread02.start()                                       #start thread
    #thread01.join()                                       #wait for thread to finish
    thread02.join()                                        #wait for thread to finish
    print('\nTime Concurrency taken                             :', time.time() - time_to_worker)

    # Create threads in a loop
    loops = 5
    threads = []
    time_to_worker02 = time.time()
    for i in range(loops):
        threads.append(Thread(target=calculate))
        threads[i].start()

    for i in range(loops):
        threads[i].join()
    print('\nTime Concurrency in loop taken                 :', time.time() - time_to_worker02)

    # Create threads in a loop with args
    threads01 = []
    time_to_worker03 = time.time()
    for i in range(loops):
        # sequential execution
        threads01.append(Thread(target=calculate_power(i+1)))
        # start threads
        threads01[i].start()

    for i in range(loops):
        threads01[i].join()
    print('\nTime with loop in sequential execution      :', time.time() - time_to_worker03)

    # Create threads in a loop with args
    threads02 = []
    time_to_worker04 = time.time()
    for i in range(loops):
        # sequential execution
        threads02.append(Thread(target=calculate_power, args=(i+1,)))
        # start threads
        threads02[i].start()

    for i in range(loops):
        threads02[i].join()
    print('\nTime with loop in parallel execution           :', time.time() - time_to_worker04)

if __name__ == "__main__":
    main()