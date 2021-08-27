def function1():

    # empty list
    list_1 = []
    print(list_1)
    print(f"type of list_1 : {type(list_1)}")

    # empty list
    list_2 = list()
    print(list_2)
    print(f"type of list_2 : {type(list_2)}")

    # list with only one item
    list_3 = [10]
    print(list_3)
    print(f"type of list_3 : {type(list_3)}")


# function1()

def function2():
    list_1 = [10,20,30,40,50]

    # iterate using for ..each
    for value in list_1:
        print(value)

    print("-*-" * 20)

    # iterate using traditional for loop
    index_positios = list(range(len(list_1)))
    for index in index_positios:
        print(f"value at {index} = {list_1[index]}")

function2()


















