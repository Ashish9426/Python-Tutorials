# pandas: excel for python
# - developed on top of numpy
# - series
#   - one dimensional array
# - dataframe


import numpy as np
import pandas as pd


def function1():
    # list
    l1 = [10, 20, 30, 40, 50]
    print(f"l1 = {l1}, type = {type(l1)}")

    # array
    a1 = np.array([10, 20, 30, 40, 50])
    print(f"a1 = {a1}, type = {type(a1)}")

    # series
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(f"s1 = {s1}, type = {type(s1)}")


# function1()


def function2():
    # series
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(s1)
    print(f"index = {s1.index}")
    print(f"values = {s1.values}")
    print(f"ndim = {s1.ndim}")
    print(f"dtype = {s1.dtype}")
    print(f"shape = {s1.shape}")

    print(f"s1[0] = {s1[0]}")
    print(f"s1[4] = {s1[4]}")


# function2()


def function3():
    cars = np.array(["i20", "innova", "i10", "nano", "X5", "Range Rover"])
    prices = np.array([7.5, 20, 5.5, 2.5, 0, 85])

    for index in range(len(cars)):
        print(f"{cars[index]} has price {prices[index]}")


# function3()


def function4():
    cars = ["i20", "innova", "i10", "nano", "X5", "Range Rover"]
    prices = [7.5, 20, 5.5, 2.5, 0, 85]

    # series using list
    s1 = pd.Series(prices, index=cars)
    print(s1)

    print(f"i20 price = {s1['i20']}")
    print(f"Range Rover price = {s1['Range Rover']}")


# function4()


def function5():
    # tuple
    numbers = (10, 20, 30, 40, 50)

    # series from tuple
    s1 = pd.Series(numbers)
    print(f"s1 = {s1}, type = {type(s1)}")


# function5()


def function6():
    # dictionary
    person = {"name": "person1", "age": 30, "email": "person1@test.com", "address": "pune"}
    print(f"person = {person}, type = {type(person)}")

    # series using dictionary
    s1 = pd.Series(person)
    print(f"s1 = {s1}, type = {type(s1)}")


function6()
