def function1():
    list_1 = [10, 20, 30, 40, 50]

    print(f"value at 0 = {list_1[0]}")
    print(f"value at 1 = {list_1[1]}")
    print(f"value at 2 = {list_1[2]}")
    print(f"value at 3 = {list_1[3]}")
    print(f"value at 4 = {list_1[4]}")

    print(f"value at -1 = {list_1[-1]}")
    print(f"value at -2 = {list_1[-2]}")
    print(f"value at -3 = {list_1[-3]}")
    print(f"value at -4 = {list_1[-4]}")
    print(f"value at -5 = {list_1[-5]}")

    print("-" * 60)
    print(f"value at 0th position = {list_1[0]}")
    print(f"value at -5th position = {list_1[-len(list_1)]}")


function1()
