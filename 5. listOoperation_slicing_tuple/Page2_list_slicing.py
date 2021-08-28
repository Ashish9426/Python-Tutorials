def function1():
    numbers = [10,20,30,40,50,60,70,80,90,100]

    number_slice = []
    # start 2
    # stop 5
    # positions = [2,3,4,5]
    positions = range(2,6)
    for index in positions:
        number_slice.append(numbers[index])

    print(number_slice)

# function1()

def function2():
    numbers = [10,20,30,40,50,60,70,80,90,100]
    # slicing (2,3,4,5)
    print(numbers[2:6])

    # slicing (4,5,6,7,8)
    print(numbers[4:9])

    # 40,50,60,70,80,90,100
    print(numbers[3:10])

    # 40,50,60,70,80,90,100
    print(numbers[3:])

    # 10,20,30,40,50
    print(numbers[0:5])

    # 10,20,30,40,50
    print(numbers[:5])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[0:10])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[0:])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[:10])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[:])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers[0:100])

    # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(numbers)

# function2()

def function3():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numbers_even = []

    positions = range(len(numbers))
    for index in positions:
        # get the valuse at even positions
        if index % 2 == 0:
            numbers_even.append(numbers[index])
    print(numbers_even)

# function3()

def function4():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # value at even positions
    print(f"numbers = {numbers[0:10:2]}")

    positions = range(len(numbers))
    for index in positions:
        # get the valuse at even positions
        if index % 2 == 0:
            print(f"Values at {index} = {numbers[index]}")

    # values at even position
    print(numbers[::2])

    # values at odd positions
    print(numbers[1:10:2])

    # values at odd positions
    print(numbers[1::2])

    # values
    print(numbers[0:10:1])
    print(numbers[::])

    # reverse the values
    print(numbers[::-1])

    # copy of the number list
    # number_1 = numbers.copy()
    # print(number_1)
    # number_1 = numbers[:]
    # print(number_1)
    # number_1 = numbers[::]
    # print(number_1)

# function4()

def function5():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # new collection with value at even position
    number_even = numbers[0:10:2]
    print(number_even)
    
function5()



