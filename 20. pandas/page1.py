import pandas as pd
import numpy as np


def function1():
    # one dimensional array
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(f"s1 = {s1}, type = {type(s1)}")
    print(f"index = {s1.index}, values = {s1.values}")


# function1()


def function2():
    # one dimensional array
    s1 = pd.Series([10, 20, 30, 40, 50])

    # +ve indexing
    # print(f"value at 0 = {s1[0]}")
    # print(f"value at 4 = {s1[4]}")

    # -ve indexing
    # not supported
    # #print(f"value at -1 = {s1[-1]}")
    # print(f"index = {s1.index}")

    # filtering
    # print(f"s1 > 30 = {s1 > 30}")
    # print(f"values > 30 = {s1[s1 > 30]}")

    # slicing
    # print(f"s1[0:2] = {s1[0:2]}")
    # print(f"s1[2:] = {s1[2:]}")
    # print(f"s1[:3] = {s1[:3]}")
    # print(f"s1[:] = {s1[:]}")


# function2()


def function3():
    s1 = pd.Series({"model": "i20", "company": "hyundai", "price": 7.5})
    print(s1)

    print(f"price = {s1['price']}")
    print(f"model = {s1['model']}")
    print(f"company = {s1['company']}")


function3()

