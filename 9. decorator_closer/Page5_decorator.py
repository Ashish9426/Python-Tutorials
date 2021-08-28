def decorate_result(function):

    def inner(p1, p2):
        print("*" * 40)
        function(p1, p2)
        print("*" * 40)

    return inner


@decorate_result
def add(p1, p2):
    print(f"addition = {p1 + p2}")


@decorate_result
def subtract(p1, p2):
    print(f"subtraction = {p1 - p2}")


# result_add = decorate_result(add)
# result_add(10, 30)
add(10, 30)


# decorate_result(add)(40, 50)
add(40, 50)

# result_subtract = decorate_result(subtract)
# result_subtract(20, 10)
subtract(20, 10)
