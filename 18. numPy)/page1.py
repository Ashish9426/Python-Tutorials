def function1():
    # list (mutable)
    numbers = [10, 20, 30, 40, 50]
    countries = ["india", "usa", "uk"]

    numbers.append(60)
    countries.append("japan")

    for number in numbers:
        print(number)

    print("-" * 50)

    for country in countries:
        print(country)


# function1()


def function2():
    # tuple (immutable)
    numbers = (10, 20, 30, 40, 50)
    countries = ("india", "usa", "uk")

    for number in numbers:
        print(number)

    print("-" * 50)

    for country in countries:
        print(country)


# function2()


def function3():
    # addition => ??
    numbers1 = [10, 20, 30, 40, 50]
    numbers2 = [60, 70, 80, 90, 100]

    numbers3 = numbers1 + numbers2
    # numbers4 = numbers1 - numbers2

    print(numbers1)
    print(numbers2)
    print(numbers3)
    # print(numbers4)


function3()
