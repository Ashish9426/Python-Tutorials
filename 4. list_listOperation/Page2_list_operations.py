def function1():
    # list
    list_1 = [10,20,30,40,50]

    # before Appending
    print(list_1)

    # Adding value 60 at the End
    list_1.append(60)

    # after appending
    print(list_1)

    # after appending 60
    list_1.append(70)
    print(list_1)

    print("Enter a value")

    #str
    str_value = input()

    # type casting to int
    value = int(str_value)

    list_1.append(value)
    # list_1.append(str_value)
    # after appending value entered by user
    print(list_1)

# function1()

def function2():
    # list
    list_1 = [10,20,30,40,50]
    print(list_1)

    # insert value after 30 or insert vale at the position 3
    list_1.insert(3, 60)
    print(list_1)

    # insert a string into the list
    list_1.append('a value 1')
    list_1.insert(2, "a value 2")

    print(list_1)
    #for value in list_1:
    #    print(value)


# function2()

def function3():
    # list
    list_1 = [10,20,30,40,50]
    print(list_1)

    # Remove the last value
    list_1.pop()
    print(list_1)

# function3()

def function4():
    # list
    list_1 = ['india','usa','uk','china',"japan"]
    print(list_1)

    # Remove china using the index from the list
    list_1.pop(3)
    print(list_1)

#function4()


def function5():
    # list
    list_1 = [10,50,20,40,50,30,50,10,30,20]
    print(list_1)

    # Remove the value 30
    list_1.remove(30)
    print(list_1)

    # Remove the value 30
    list_1.remove(30)
    print(list_1)

    # Remove the value 30
    list_1.remove(30)
    print(list_1)

# function5()

def function6():
    # list
    list_1 = ['india','usa','uk','china',"japan"]
    print(list_1)

    # Remove china using the index from the list
    # list_1.pop(3)
    # print(list_1)

    # Remove china using the index from the list
    list_1.remove("china")
    print(list_1)

# function6()

def function7():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    # find occurences of 30
    count_30 = list_1.count(30)
    print(f"30 repeated {count_30} times")

    for index in range(count_30):
        list_1.remove(30)
    print(list_1)

    # find occurences of 50
    count_50 = list_1.count(50)
    print(f"50 repeated {count_50} times")

    for index in range(count_50):
        list_1.remove(50)
    print(list_1)


# function7()

def function8():
    # list
    fruits = ["apple","banana","orange","jackfruits","apple"]

    # apple_count = fruits.count('apple')
    # print(f"Apple repeated {apple_count} times")

    print(f"Apple repeated {fruits.count('apple')} times")

    apple_count = fruits.count('apple')
    for index in range(apple_count):
        fruits.remove("apple")

    print(fruits)

# function8()


def function9():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    print(f"50 repeated {list_1.count(50)} times")

    # position_50 = list_1.index(50)
    # print(f"50 appears at position {position_50}")

    # position_50 = list_1.index(50, 2)
    # print(f"50 appears at position {position_50}")

    # position_50 = list_1.index(50, 4)
    # print(f"50 appears at position {position_50}")

    # position_50 = list_1.index(50, 5)
    # print(f"50 appears at position {position_50}")

    position = 0
    count_50 = list_1.count(50)

    for index in range(count_50):
        position_50 = list_1.index(50, position)
        print(f"50 appears at {position_50}")

        # search for 50 from the next position
        position = position_50 + 1


# function9()

def function10():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    # create copy of list_1
    list_1_sorted_asc = list_1.copy()

    # inplace sort
    # modifies the original collection
    list_1_sorted_asc.sort()
    print(list_1_sorted_asc)

    print("-*-" * 20)

    # sort in descending order
    list_1_sorted_asc.reverse()
    print(list_1_sorted_asc)

    print("-*-" * 20)

    # create a copy of list_1
    # list_1_sorted_desc = list_1.copy()

    # inplace sort
    # list_1_sorted_desc.sort(reverse=True)
    # print(list_1_sorted_desc)

    # print(list_1)


# function10()

def function11():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    list_1.reverse()
    print(list_1)

#function11()

def function12():
    # list
    list_1 = [10, 50, 20, 40, 50, 30, 50, 10, 30, 20]
    print(list_1)

    # remove all the values
    list_1.clear()
    print(list_1)

# function12()

def function13():
    # list
    list_1 = [10,20,30,40,50]
    list_2 = [60,70,80,90,100]

    print(list_1)

    # append another list
    list_1.append(list_2)
    #list_1.extend(list_2)

    print(list_1)

    print(len(list_1))

# function13()

def function14():
    # list
    list_1 = [10, 20, 30, 40, 50]
    list_2 = [60, 70, 80, 90, 100]
    print(list_1)
    print(list_2)

    #list_3 = list_1.extend(list_2)
    #print(list_3)

    list_3 = list_1.copy()
    list_3.extend(list_2)
    print(list_3)

function14()