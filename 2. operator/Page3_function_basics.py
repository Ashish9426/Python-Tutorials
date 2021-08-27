# function
def empty_function():
    pass

def function1():
    print("inside function function 1")
    print("this is function body")

# function1()

def function2(param):
    # param = 10
    # param = 10.56
    # param = "steve"
    # param = True
    print("inside function2")
    print(f"param = {param}, data type = {type(param)}")

# function2(10)
# function2(10.25)
# function2("steve")
# function2(True)


def add(p1, p2):
    """
    this function will add two parameters
    :param p1: integer 1st argument
    :param p2: integer 2nd argument
    :return: nothing
    """
    print("inside add function")
    addition = p1 + p2
    print(f"addition = {addition}")

# dunder doc
# print(add.__doc__)

# add(10, 20)
# add("hello", "python")
# add(10.47, 45.7)

def function3():
    """
    documentation string (docstring)
    this is a test function
    :return: nothing
    """
    print("inside function3")


# function3()
# print(function3.__doc__)


def multiply(p1, p2):
    """
    multiply two parameters
    :param p1: int
    :param p2: int
    :return: multiplication of two parameters
    """
    multiplication = p1 * p2
    return multiplication

# print(multiply.__doc__)
answer = multiply(40, 60)
print(f"answer = {answer}, type = {type(answer)}")


def function4():
    print("inside function4")


value = function4()
print(f"value = {value}")







