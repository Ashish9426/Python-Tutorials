def function1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # find out the even numbers
    numbers_even = list(filter(lambda x: x % 2 == 0, numbers))

    # square of even numbers
    squares_even = list(map(lambda x: x ** 2 , numbers_even))

    print(squares_even)


# function1()

def function2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # find out the odd numbers
    numbers_odd = list(filter(lambda x: x % 2 != 0, numbers))

    # get the cube of every odd number
    cube_odd = list(map(lambda x: x ** 3, numbers_odd))

    print(numbers_odd)
    print(cube_odd)


function2()

