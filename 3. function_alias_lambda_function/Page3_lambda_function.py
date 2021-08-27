def square(number):
    return number ** 2


# function alias
mySquare = square
print(f"square of 9 = {square(9)}")

# lambda function

cube = lambda number:number**3
print(f"cube of 9 = {cube(9)}")
print(f"cube = {cube}")
print(f"type of cube = {type(cube)}")

def add(p1, p2):
    return p1 + p2

myAdd = add

addition = add(30, 30)
print(f"Addition of 30 and 40 = {addition}")

addition = myAdd(50, 60)
print(f"Addition of 50 and 60 = {addition}")


# inline function
# add = lambda (p1, p2): return p1 + p2
lambda_add = lambda p1, p2: p1 + p2
print(f"addition of 10 and 20 = {lambda_add(10, 20)}")


# lambda for multiply two numbers
# accepts two values and returns multiplication of them
multiply = lambda x, y: x * y
print(f"multiplication = {multiply(10, 40)}")