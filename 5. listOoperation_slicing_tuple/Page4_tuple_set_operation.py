def function1():
    # list
    numbers_1 = [10,20,30,10,20,30,10,20,30]
    print(f"number_1 = {numbers_1}, type = {type(numbers_1)}")

    # tuple
    numbers_2 = 10, 20, 30, 10, 20, 30, 10, 20, 30
    print(f"number_2 = {numbers_2}, type = {type(numbers_2)}")

    # set
    numbers_3 = {10, 20, 30, 10, 20, 30, 10, 20, 30}
    print(f"number_3 = {numbers_3}, type = {type(numbers_3)}")

    # list
    numbers_4 = [10,28,72,29,10,20,49,20,40,58,60]
    print(f"number_4 = {numbers_4}, type = {type(numbers_4)}")

    set_4 = set(numbers_4)
    print(f"numbers_4 = {numbers_4}")
    print(f"unique values = {set_4}")

# function1()

def function2():
    s1 = {10,20,30,40}
    s2 = {30,40,50,60}

    print(f"s1 union s2 = {s1.union(s2)}")
    print(f"s2 union s1 = {s2.union(s1)}")
    print(f"s1 intersection s2 = {s1.intersection(s2)}")
    print(f"s2 intersection s1 = {s2.intersection(s1)}")
    print(f"s2 - s1 = {s2.difference(s1)}")
    print(f"s1 - s2 = {s1.difference(s2)}")

# function2()

def function3():
    s1 = {10,20,30,40,50}
    print(s1)

    # add
    s1.add(60)
    s1.add(60)
    s1.add(60)
    s1.add(60)
    s1.add(60)
    s1.add(70)
    s1.add(70)
    s1.add(70)
    s1.add(70)
    s1.add(80)
    s1.add(80)
    s1.add(80)
    s1.add(80)
    s1.add(80)

    print(s1)

# function3()

def function4():
    s1 = {10, 20, 30, 40, 50}
    print(s1)

    # remove a value
    # 1.remove(30)
    # print(s1)

    # remove will raise an exception when a value is missing
    s1.remove(100)
    print(s1)

    # remove a value
    s1.discard(50)
    print(s1)

    # discard will NOT raise any exception if the value is missing
    s1.discard(100)
    print(s1)


function4()