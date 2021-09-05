def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]

    # for number in numbers:
    #     print(number)

    # iterable
    # - object that can be iterated
    # - list object is iterable

    # iterator
    # - one who iterates
    # - list_iterator is an iterator

    iterator = iter(numbers)
    print(iterator)
    try:
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
    except StopIteration:
        print("end of the list")


function1()