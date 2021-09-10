import pandas as pd
import numpy as np


def function1():
    # list:: one dimensional array
    l1 = [10, 20, 30, 40, 50]
    print(f"l1 = {l1}, type = {type(l1)}")
    print("-" * 80)

    # array: one dimensional array
    a1 = np.array([10, 20, 30, 40, 50])
    print(f"a1 = {a1}, type = {type(a1)}")
    print("-" * 80)

    # series: one dimensional array
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(f"s1 -- type = {type(s1)} -- ")
    print(s1)
    print("-" * 80)

    # data frame: multi-dimensional array
    df1 = pd.DataFrame([10, 20, 30, 40, 50])
    print(f"df1 -- type = {type(df1)} --")
    print(df1)
    print("-" * 80)


# function1()


def function2():
    # data frame: multi-dimensional array
    df = pd.DataFrame([10, 20, 30, 40, 50])
    print("---- df ----")
    print(df)
    print("---- df ----")

    print(f"dimensions = {df.ndim}")
    print(f"shape = {df.shape}")
    print(f"data types = {df.dtypes}")


# function2()


def function3():
    df = pd.DataFrame([
        [10, 20],
        [30, 40],
        [50, 60],
        [70, 80],
        [90, 100]
    ])
    print(f"type = {type(df)}")
    print(f"dimensions = {df.ndim}")
    print(f"shape = {df.shape}")
    print(df)

    print("-" * 80)
    df1 = pd.DataFrame([
        [10, 20, 30, 40, 50],
        [60, 70, 80, 90, 100]
    ])
    print(f"type = {type(df1)}")
    print(f"dimensions = {df1.ndim}")
    print(f"shape = {df1.shape}")
    print(df1)


# function3()


def function4():
    df = pd.DataFrame([
        [10, 20],
        [30, 40],
        [50, 60],
        [70, 80],
        [90, 100],
        [110, 120],
        [130, 140],
        [150, 160],
        [170, 180]
    ])

    print(df.ndim)
    print(df.dtypes)
    print(df.shape)
    # print(df.head(3))
    # print(df.tail(3))
    print("-" * 40)
    print(df.info())
    print("-" * 40)
    print(df.describe())
    print("-" * 40)


# function4()


def function5():
    df = pd.DataFrame([
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5}
    ])

    print(df)


#function5()
