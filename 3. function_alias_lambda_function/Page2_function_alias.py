num = 100
print(f"num = {num}, type = {type(num)}")

num2 = num
print(f"num2 = {num2}, type = {type(num2)}")

num = 300

print(f"num = {num}, type = {type(num)}")
print(f"num2 = {num2}, type = {type(num2)}")


def function1():
    print("inside function1")


print(f"function1 = {function1}")
print(f"type of function1 = {type(function1)}")


# function alias
# another name given to existing function
# variable to a function
myFunction = function1
print(f"myFunction = {myFunction}")
print(f"type of myFunction = {type(myFunction)}")

function1()
myFunction()

myFunction2 = function1
print(f"myFunction2 = {myFunction2}")

myFunction3 = function1
print(f"myFunction3 = {myFunction3}")
