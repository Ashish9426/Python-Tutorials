def function1():
    # mutable
    s1 = {10, 20, 30, 40, 50}

    s1.add(60)
    s1.add(60)
    s1.add(60)

    print(s1)

    s1.remove(20)
    s1.discard(40)

    print(s1)

# function1()

def function2():
    # immutable
    s1 = frozenset([10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30])
    print(f"s1 = {s1}, type = {type(s1)}")

function2()
