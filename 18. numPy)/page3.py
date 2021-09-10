import numpy as np


def function1():
    # list
    l1 = [1, 2, 3, 4, 5]
    print([num + 10 for num in l1])
    # print(l1 + 10)


# function1()


def function2():
    a1 = np.array([1, 2, 3, 4, 5])

    # broadcast mathematical operators
    print(a1 + 10)
    print(a1 - 10)
    print(a1 * 10)
    print(a1 / 10)

    # broadcast comparison operators
    print(a1 > 2)
    print(a1 >= 2)
    print(a1 < 2)
    print(a1 <= 2)
    print(a1 == 2)
    print(a1 != 2)

    # broadcast logical operators
    print(a1 & 2)
    print(a1 | 2)


function2()


def function3():
    a1 = np.array([1, 2, 3, 4, 5])
    a2 = np.array([1, 2, 3, 4, 5])

    # broadcast operators
    print(f"{a1} + {a2} = {a1 + a2}")
    print(f"{a1} - {a2} = {a1 - a2}")
    print(f"{a1} * {a2} = {a1 * a2}")
    print(f"{a1} / {a2} = {a1 / a2}")
    print(f"{a1} % {a2} = {a1 % a2}")

    a3 = np.array([True, True, False, False])
    a4 = np.array([True, False, True, False])

    # broadcast logical operators
    print(f"{a3} & {a4} = {a3 & a4}")
    print(f"{a3} | {a4} = {a3 | a4}")

    # print(f"{a3} && {a4} = {a3 and a4}")
    # print(f"{a3} || {a4} = {a3 or a4}")


#function3()
