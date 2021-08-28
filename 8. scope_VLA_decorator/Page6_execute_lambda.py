def add(p1, p2):
    # print(f"addition = {p1 + p2}")
    return p1 + p2


def subtract(p1, p2):
    # print(f"subtraction = {p1 - p2}")
    return p1 - p2


def execute(function):
    print('-' * 20)
    print(f"result = {function(20, 10)}")
    print('-' * 20)


# print(f"{add(20, 10)}")

execute(add)
execute(subtract)
multiply = lambda x, y : x * y
print(f"multiply = {multiply}, type = {type(multiply)}")
execute(multiply)
execute(lambda x, y: x / y)


# add(10, 20)
# ------------------
# addition = 30
# ------------------

# subtract(20, 10)
# ------------------
# subtraction = 10
# ------------------
