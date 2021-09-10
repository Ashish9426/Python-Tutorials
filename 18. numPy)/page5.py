import numpy as np


def function1():
    # array
    # - contiguous memory allocation
    # - collection of similar values
    a1 = np.array([10, 20, 30, 40, 50])
    print(f"a1 = {a1}, type = {type(a1)}")
    print(f"type of value in a1 = {a1.dtype}")

    a2 = np.array([10., 20., 30., 40., 50.])
    print(f"a2 = {a2}, type = {type(a2)}")
    print(f"type of value in a2 = {a2.dtype}")

    a3 = np.array(["str123", "str224"])
    print(f"a3 = {a3}, type = {type(a3)}")
    print(f"type of value in a3 = {a3.dtype}")

    a4 = np.array([10, 20.0, "str1234"])
    print(f"a4 = {a4}, type = {type(a4)}")
    print(f"type of value in a4 = {a4.dtype}")


function1()


def function2():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # indexing
    print(f"a1[0] = {a1[0]}")
    print(f"a1[-1] = {a1[-1]}")

    # slicing
    print(f"a1[0:3] = {a1[0:3]}")


# function2()


def function3():
    a1 = np.array([10, 20, 30, 40, 50])

    # [20, 50]
    index_position = [1, 4]
    print(a1[index_position])

    # [20, 50]
    print(a1[[1, 4]])

    # [20, 50]
    print(a1[[False, True, False, False, True]])


# function3()


def function4():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    print(a1 > 40)
    print(a1[[False, False, False, False,  True, True,  True,  True,  True,  True]])

    # filtering
    # print(a1[a1 > 40])
    print(a1[a1 < 60])

    salaries = np.array([10, 15, 7, 8, 20, 50, 49])
    print(salaries[salaries > 20])


#vfunction4()
