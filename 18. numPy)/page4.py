import numpy as np


def function1():
    a1 = np.array([10, 20, 30, 40, 50, 60], dtype=np.int8)
    print(f"a1 = {a1}, type = {type(a1)}")
    print(f"item size = {a1.itemsize}")
    print(f"data type = {a1.dtype}")
    print(f"number of values = {a1.size}")
    print(f"total memory = {a1.itemsize * a1.size}")
    print(f"total memory = {a1.nbytes}")
    print(f"number of dimensions = {a1.ndim}")
    print(f"shape = {a1.shape}")

    print('-' * 50)

    a2 = a1.reshape((2, 3))
    print(f"a2 = {a2}, type = {type(a2)}")
    print(f"item size = {a2.itemsize}")
    print(f"data type = {a2.dtype}")
    print(f"number of values = {a2.size}")
    print(f"total memory = {a2.itemsize * a2.size}")
    print(f"total memory = {a2.nbytes}")
    print(f"number of dimensions = {a2.ndim}")
    print(f"shape = {a2.shape}")

    print('-' * 50)

    a3 = a1.reshape((3, 2))
    print(f"a3 = {a3}, type = {type(a3)}")
    print(f"item size = {a3.itemsize}")
    print(f"data type = {a3.dtype}")
    print(f"number of values = {a3.size}")
    print(f"total memory = {a3.itemsize * a3.size}")
    print(f"total memory = {a3.nbytes}")
    print(f"number of dimensions = {a3.ndim}")
    print(f"shape = {a3.shape}")

    print('-' * 50)

    a4 = a1.reshape((6, 1))
    print(f"a4 = {a4}, type = {type(a4)}")
    print(f"item size = {a4.itemsize}")
    print(f"data type = {a4.dtype}")
    print(f"number of values = {a4.size}")
    print(f"total memory = {a4.itemsize * a4.size}")
    print(f"total memory = {a4.nbytes}")
    print(f"number of dimensions = {a4.ndim}")
    print(f"shape = {a4.shape}")

    print('-' * 50)

    a5 = a1.reshape((1, 6))
    print(f"a5 = {a5}, type = {type(a5)}")
    print(f"item size = {a5.itemsize}")
    print(f"data type = {a5.dtype}")
    print(f"number of values = {a5.size}")
    print(f"total memory = {a5.itemsize * a5.size}")
    print(f"total memory = {a5.nbytes}")
    print(f"number of dimensions = {a5.ndim}")
    print(f"shape = {a5.shape}")


function1()
