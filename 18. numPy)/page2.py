import numpy as np
import sys


def function1():
    # python list
    list1 = [10, 20, 30, 40, 50]
    print(f"list1 = {list1}, type = {type(list1)}")
    print(f"item size = {sys.getsizeof(list1[0])}")
    print(f"number of values = {len(list1)}")
    print(f"total memory = {len(list1) * sys.getsizeof(list1[0])}")
    #print(f"Total Memory size = {sys.getsizeof(list1)}")

    print("-" * 80)

    # numpy array => immutable
    a1 = np.array([10, 20, 30, 40, 50])
    print(f"a1 = {a1}, type = {type(a1)}")
    print(f"item size = {a1.itemsize}")
    print(f"data type = {a1.dtype}")
    print(f"number of values = {a1.size}")
    print(f"total memory = {a1.itemsize * a1.size}")

    print("-" * 80)

    a2 = np.array([10, 20, 30, 40, 50], dtype=np.int32)
    print(f"a2 = {a2}, type = {type(a2)}")
    print(f"item size = {a2.itemsize}")
    print(f"data type = {a2.dtype}")
    print(f"number of values = {a2.size}")
    print(f"total memory = {a2.itemsize * a2.size}")

    print("-" * 80)

    a3 = np.array([10, 20, 30, 40, 50], dtype=np.int16)
    print(f"a3 = {a3}, type = {type(a3)}")
    print(f"item size = {a3.itemsize}")
    print(f"data type = {a3.dtype}")
    print(f"number of values = {a3.size}")
    print(f"total memory = {a3.itemsize * a3.size}")

    print("-" * 80)

    a4 = np.array([10, 20, 30, 40, 50], dtype=np.int8)
    print(f"a4 = {a4}, type = {type(a4)}")
    print(f"item size = {a4.itemsize}")
    print(f"data type = {a4.dtype}")
    print(f"number of values = {a4.size}")
    print(f"total memory = {a4.itemsize * a4.size}")


# function1()


def function2():
    a1 = np.array([10, 20, 30, 40, 50, 60], dtype=np.int16)
    print(f"a1 = {a1}, type = {type(a1)}")
    print(f"item size = {a1.itemsize}")
    print(f"data type = {a1.dtype}")
    print(f"number of values = {a1.size}")
    print(f"total memory = {a1.itemsize * a1.size}")
    print(f"total memory = {a1.nbytes}")
    print(f"number of dimensions = {a1.ndim}")
    print(f"shape = {a1.shape}")


# function2()


def function3():
    a1 = np.array(
        [
            [10, 20, 30],
            [40, 50, 60]
        ], dtype=np.int16)
    print(f"a1 = {a1}, type = {type(a1)}")
    print(f"item size = {a1.itemsize}")
    print(f"data type = {a1.dtype}")
    print(f"number of values = {a1.size}")
    print(f"total memory = {a1.itemsize * a1.size}")
    print(f"total memory = {a1.nbytes}")
    print(f"number of dimensions = {a1.ndim}")
    print(f"shape = {a1.shape}")


#function3()
