# scope: global
num = 100
print(f"outside of any function num = {num}")


def function1():
    print("inside function 1")
    print(f"num = {num}")

    # scope: local
    first_name = "steve"
    print(f"first name = {first_name}")


function1()

# can not access first_name here as it is a local variable of function1
# print(f"outside of function1: first name = {first_name}")


def function2():
    print("inside function 2")
    print(f"num = {num}")

    # can not access first_name here as it is a local variable of function1
    # print(f"first name = {first_name}")


function2()
