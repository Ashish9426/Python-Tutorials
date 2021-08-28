def function1():
    numbers = [1,2,3,4]
    for number in numbers:
        print(f"Square = {number**2}")

# function1()

def function2():
    numbers = [1,2,3,4,5]
    # reasons to reject the following collections:
    # - dictionary: collection of key-value pairs
    # - set       : set does not follow insertion order
    # - tuple     : immutable collection

    # reason to go with list
    # - list      : mutable and follows insertion order

    squares = []
    for number in numbers:
        squares.append(number**2)
    print(numbers)
    print(squares)

# function2()

def get_squares(number):
    return number**2

def function3():
    numbers = [1,2,3,4,5]

    squares = []
    for number in numbers:
        squares.append(get_squares(number))
    print(numbers)
    print(squares)

# function3()

def function4():
    numbers = [1,2,3,4,5]

    # used to get square of a number
    square = lambda x: x**2

    squares = []
    for number in numbers:
        squares.append(square(number))
    print(numbers)
    print(squares)

# function4()

def function5():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    squares = tuple(map(get_squares, numbers))

    print(numbers)
    print(squares)

# function5()

def function6():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    square = lambda x: x**2
    squares = tuple(map(square, numbers))

    print(numbers)
    print(squares)

# function6()

def function7():
    temperature_C = [38,39,32,36,37,40]
    temperature_F = tuple(map(lambda x: (x * (9/5) + 32), temperature_C))

    print(temperature_C)
    print(temperature_F)

# function7()

def function8():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squares = tuple(map(lambda x: x**2, numbers))

    print(numbers)
    print(squares)

# function8()

def function9():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "X5", "company": "BMW", "price": 35.5},
        {"model": "Inova", "company": "Toyota", "price": 20.5},
    ]

    # [
    #     {"model": "i20", "price": 7.5},
    #     {"model": "i10", "price": 5.5},
    #     {"model": "nano", "price": 2.5},
    #     {"model": "X5", "price": 35.5},
    #     {"model": "Inova", "price": 20.5},
    # ]

    cars_new = list(map(lambda car: {"model": car['model'], "price": car['price'], "company": car['company']}, cars))
    print(cars)
    print(cars_new)


# function9()

def function10():
    persons = [
        {"name": "person1", "address": "pune", "age": 40, "email": "person1@test.com"},
        {"name": "person2", "address": "mumbai", "age": 20, "email": "person2@test.com"},
        {"name": "person3", "address": "nashik", "age": 30, "email": "person3@test.com"},
        {"name": "person4", "address": "satara", "age": 10, "email": "person4@test.com"}
    ]

    # [ {"name": "", address: ""},  ... ]
    persons_new = list(map(lambda person: {"name": person['name'], "address": person['address']}, persons))
    print(persons)
    print(persons_new)


function10()


