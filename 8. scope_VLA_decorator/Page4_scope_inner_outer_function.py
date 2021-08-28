# global
num = 100


# global function
# outer function
def function1():
    print("inside function1")

    # local
    salary = 10.56

    # local function
    # inner function
    def inner_function1():
        print("inside inner_function")

    print(f"inner_function1 = {inner_function1}, type = {type(inner_function1)}")
    inner_function1()

# function1()
# inner_function1()
# print(f"function1 = {function1}, type = {type(function1)}")

def outer():
    # declared by outer
    outer_variable = 10

    print(f"inside function outer")
    print(f"outer_variable = {outer_variable}")

    def inner1():
        print(f"inside inner 1")

        # inner function can access all the members of outer function
        print(f"outer_variable = {outer_variable}")

    inner1()

    def inner2():
        print(f"inside inner 2")

        inner_2_variable = 100
        print(f"inner_2_variable = {inner_2_variable}")

    inner2()

    # outer function can not access any of the inner function members
    # print(f"inside outer, inner_2_variable = {inner_2_variable}")


outer()

