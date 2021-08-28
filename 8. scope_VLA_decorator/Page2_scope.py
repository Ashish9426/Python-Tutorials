# scope: global
num = 100

# num = 100
print(f"before calling function1 num = {num}")


def function1():
    print("inside function1")

    # function1 declares a new variable num with local scope
    # scope: local
    num = 500
    print(f"num = {num}")


function1()


# num = 500
print(f"after calling function1 num = {num}")


def function2():
    print(f"inside function2")

    # to modify the global variable value
    # stops function2 from creating a local copy of num
    global num

    # modify the global num's value
    num = 600
    print(f"num = {num}")


function2()


print(f"after calling function2 num = {num}")
