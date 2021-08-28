def function1():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    numbers.append(60)
    print(numbers)

    numbers.insert(3, 70)
    print(numbers)

    numbers.pop()
    print(numbers)

    numbers.pop(2)
    print(numbers)

    numbers.remove(20)
    print(numbers)


# function1()

def function2():
    numbers = [10, 30, 10, 50, 50, 70, 60, 20, 30, 40, 50]

    count_50 = numbers.count(50)
    print(f"50 repeated {count_50} times")

    index_70 = numbers.index(70)
    print(f"70 appears at {index_70} position")

    numbers_reverse = numbers.copy()
    numbers_reverse.reverse()
    print(numbers_reverse)

    numbers_sorted_asc = numbers.copy()
    numbers_sorted_asc.sort()
    print(numbers_sorted_asc)

    numbers_sorted_desc = numbers.copy()
    numbers_sorted_desc.sort(reverse=True)
    print(numbers_sorted_desc)

# function2()

def function3():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # positive
    print(f"value at first position = {numbers[0]}")
    print(f"value at last position = {numbers[len(numbers) - 1]}")

    # negative
    print(f"value at first position = {numbers[-len(numbers)]}")
    print(f"value at last position = {numbers[-1]}")


function3()


