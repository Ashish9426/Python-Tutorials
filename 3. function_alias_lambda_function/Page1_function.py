def function1():
    """
    this is a function1
    :return:
    """
    print("inside funtion1")
    print("function1 .__doc__")

# print(function1.__doc__)
# function1()

def function2(p1, p2):
    print("inside function2")
    print(f"p1 = {p1}, type = {type(p1)} ")
    print(f"p2 = {p2}, type = {type(p2)} ")

# function2(10, 20)
# function2(p1=10, p2=20)
# function2(p2=20, p1=10)
# function2(10, p2=20)


num = 10
print(f"num = {num}, type = {type(num)}")

num = 200
print(f"num = {num}, type = {type(num)}")

print(f"function1 = {function1}, type = {type(function1)}")
print(f"function2 = {function2}, type = {type(function2)}")