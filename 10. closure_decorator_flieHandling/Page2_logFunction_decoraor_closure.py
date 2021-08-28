# closure
def log(function):

    # variable length argument function
    def inner(*args, **kwargs):
        print("-" * 40)
        print(f"inside function named = {function.__name__}")
        print(f"args = {args}")
        print(f"kwargs = {kwargs}")

        function(*args, **kwargs)
        print("-" * 40)

    return inner


@log
def add(*args, **kwargs):
    # print(f"addition = {p1 + p2}")
    sum = 0
    for number in args:
        sum += number
    print(f"sum = {sum}")


# log_add = log(add)
# log_add(10, 20)
# add(10, 20)
# add(20, p3=10)


@log
def divide(p1, p2):
    if p2 == 0:
        print("you can not divide any number  by zero")
    else:
        print(f"division = {p1 / p2}")


divide(30, 20)
divide(p2=40, p1=10)
divide(10, 0)

@log
def square(number):
    print(f"square of {number} = {number ** 2}")


#log_square = log(square)
#log_square(10)
#square(10)
#square(number=5)
#square()


