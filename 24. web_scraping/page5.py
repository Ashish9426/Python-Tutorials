import time
import threading


def function1():
    print("reading data from a file")
    time.sleep(10)
    print(f"reading data completed")


def function2():
    print("started performing calculation")
    multiplication = 12343345 * 45343535
    time.sleep(10)
    print(f"multiplication = {multiplication}")


def sync_execution():
    # synchronous (sequential)
    function1()
    function2()


# sync_execution()


def async_execution():
    # asynchronous (non-sequential)

    # create threads
    thread1 = threading.Thread(target=function1)
    thread2 = threading.Thread(target=function2)

    # start the threads
    thread1.start()
    thread2.start()


async_execution()


