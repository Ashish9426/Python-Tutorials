def function1():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    for number in numbers:
        if number % 2 == 0:
            print(number)


# function1()

def function2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_nubers = []

    for number in numbers:
        if number % 2 == 0:
            even_nubers.append(number)
    print(even_nubers)
    print(numbers)

# function2()

def function3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers_1 = list(map(lambda x: x % 2 ==0, numbers))

    even_numbers_2 = list(filter(lambda x: x % 2 ==0, numbers))

    print(numbers)
    print(even_numbers_1)
    print(even_numbers_2)

# function3()

def function4():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(numbers)
    print(odd_numbers)

# function4()

def function5():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "X5", "company": "BMW", "price": 35.5},
        {"model": "Inova", "company": "Toyota", "price": 20.5},
    ]

    # price < 10
    affordable_cars = list(filter(lambda car: car['price'] < 10, cars))
    print(cars)
    print(affordable_cars)

# function5()

def function6():
    persons = [
        {"name": "person1", "address": "pune", "age": 40, "email": "person1@test.com"},
        {"name": "person2", "address": "mumbai", "age": 20, "email": "person2@test.com"},
        {"name": "person3", "address": "nashik", "age": 30, "email": "person3@test.com"},
        {"name": "person4", "address": "satara", "age": 10, "email": "person4@test.com"}
    ]

    persons_vote = list(filter(lambda person: person['age'] >= 18, persons))

    print(persons_vote)

    #for index in persons_vote:
    #    print(f"valid person = {index}")

    # AttributeError: 'list' object has no attribute 'key'
    keys = persons_vote.key
    for key in keys:
       print(f"{key} = {persons_vote[key]}")




function6()


