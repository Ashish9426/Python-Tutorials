def outer():
    print("inside outer")

    # local
    num = 100
    print(f"num = {num}")

    # local
    def inner():
        print("inside inner")

        # inner can access all the members of outer function
        print(f"num = {num}")

    inner()


# outer()

def add(p1, p2):
    return f"{p1} + {p2} = {p1 + p2}"


def subtract(p1, p2):
    return f"{p1} - {p2} = {p1 - p2}"


def execute(function):
    print("-" * 40)
    print(function(20, 10))
    print("-" * 40)


# print(add(20, 10))
# print(subtract(20, 10))

execute(add)
execute(subtract)

