import time
import numpy as np


def calculate_time(function):

    def inner(*args, **kwargs):
        time1 = time.time()
        function(*args, **kwargs)
        time2 = time.time()
        difference = time2 - time1
        print(f"time taken : {difference}")

    return inner


@calculate_time
def my_function():
    numbers = range(1, 10000000)
    for number in numbers:
        square = number ** 2


my_function()
