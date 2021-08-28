def function1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squares = []
    for number in numbers:
        squares.append(number ** 2)

    print(squares)


# function1()

def function2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squares = list(map(lambda x: x ** 2, numbers))
    print(squares)


# function2()

def function3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # list comprehension
    # return every number from the numbers collection
    numbers_1 = [number for number in numbers]

    print(numbers)
    print(numbers_1)

    squares = [number ** 2 for number in numbers]
    print(squares)

    cubes = [x ** 3 for x in numbers]
    print(cubes)

    power_4 = [x ** 4 for x in numbers]
    print(power_4)


# function3()

def function4():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    numbers_even = list(filter(lambda x: x % 2 == 0, numbers))
    print(numbers)
    print(numbers_even)

    numbers_even_lc = [x for x in numbers if x % 2 == 0]
    print(numbers_even_lc)


# function4()

def function5():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # squares_even_map_filter = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    # print(squares_even_map_filter)

    # squares_even_lc = [x ** 2 for x in numbers if x % 2 == 0]
    # print(squares_even_lc)

    cube_odd_lc = [x ** 3 for x in numbers if x % 2 != 0]
    print(cube_odd_lc)


function5()

def function6():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "X5", "company": "BMW", "price": 35.5},
        {"model": "Inova", "company": "Toyota", "price": 20.5},
    ]

    cars_non_affordable = [car for car in cars if car['price'] > 10]
    print(cars_non_affordable)


function6()






