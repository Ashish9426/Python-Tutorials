def function1():
    # single dimensional
    list1 = [10, 20, 30, 40, 50]

    # multi dimensional
    # collection of collections
    list2 = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]
    print(f"list2[0] = {list2[0]}")
    print(f"list2[1] = {list2[1]}")
    print(f"list2[2] = {list2[2]}")
    print("-" * 20)
    print(f"list2[0][0] = {list2[0][0]}")
    print(f"list2[0][1] = {list2[0][1]}")
    print(f"list2[1][0] = {list2[1][0]}")
    print(f"list2[1][1] = {list2[1][1]}")
    print(f"list2[2][0] = {list2[2][0]}")
    print(f"list2[2][1] = {list2[2][1]}")


# function1()

def function2():
    # list of lists
    list1 = [
        [10, 20],
        [30, 40, 50],
        [60, 70, 80, 90, 100]
    ]

    for row in list1:
        for col in row:
            print(f"value = {col}")
        print("-*-" * 10)

    for row in range(len(list1)):
        print(f"row at position = {row} = {list1[row]}")

        # inner list
        tmp_list = list1[row]
        for col in range(len(tmp_list)):
            print(f"value at [{row}][{col}] = {list1[row][col]}")

        print("-" * 20)


# function2()

def function3():
    # list of tuples
    persons = [
        ("person1", 40, "pune"),
        ("person2", 20, "mumbai"),
        ("person3", 10, "nashik")
    ]

    #for row in persons:
    #     print(row)
    #     print(f"name = {row[0]}")
    #     print(f"age = {row[1]}")
    #     print(f"address = {row[2]}")
    #     print("-" * 20)

    #for row in persons:
    #     name, age, address = row
    #    print(f"name = {name}")
    #     print(f"age = {age}")
    #     print(f"address = {address}")
    #     print("-" * 20)


    #for name, age, address in persons:
    #     print(f"name = {name}")
    #     print(f"age = {age}")
    #     print(f"address = {address}")
    #     print("-" * 20)

    for (name, age, address) in persons:
        print(f"name = {name}")
        print(f"age = {age}")
        print(f"address = {address}")
        print("-" * 20)


# function3()

def function4():
    # tuple
    t1 = 10, 20, 30, 40

    print(t1[0])
    print(t1[1])
    print(t1[2])
    print(t1[3])

    print("-" * 20)

    n1, n2, n3, n4 = 10, 20, 30, 40
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"n3 = {n3}")
    print(f"n4 = {n4}")


# function4()

def function5():
    person = "person1", 40, "person1@test.com"

    print(f"name: {person[0]}")
    print(f"age: {person[1]}")
    print(f"address: {person[2]}")

    print("-" * 30)

    # name, age, email = "person1", 40, "person1@test.com"
    (name, age, email) = ("person1", 40, "person1@test.com")
    # name, age, email = person
    # (name, age, email) = person

    print(f"name: {name}")
    print(f"age: {age}")
    print(f"address: {email}")


# function5()

def function6():
    # n1 = 10
    # n2 = 20

    n1, n2 = 10, 20
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")

    # swap
    n2, n1 = n1, n2
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")


# function6()

def function7():
    # list of dictionaries
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i20", "company": "hyundai", "price": 7.5}
    ]

    for car in cars:
        print(f"model: {car['model']}")
        print(f"company: {car['company']}")
        print(f"price: {car['price']}")
        print('-' * 20)


function7()