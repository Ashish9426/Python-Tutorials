# Collection
# Array or collection

# List          =>  []
# tupple        =>  ()
# Set           =>  {}
# Dictionary    =>  {}

def function1():
    # array of numbers (int)
    numbers = [10,20,30,40,50,60,70,80,90,100]
    print(numbers)
    print(f"type of numbers = {type(numbers)}")
    print(f"Numbers of value in numbers = {len(numbers)}")

# function1()
    # using for loop:
    # for number in numbers:
    #    print(f"number = {number}")

#function1()
    # using subscript
    # print(f"value at 0th position = {numbers[0]}")
    # print(f"value at 1st position = {numbers[1]}")
    # print(f"value at 2nd position = {numbers[2]}")
    # print(f"value at 3rd position = {numbers[3]}")
    # print(f"value at 4th position = {numbers[4]}")

#function1()

    # traditional for loop
    # for (int index = 0; index < 5; index++) { .. }
    # index_positions = [0, 1, 2, 3, 4, 6, 7, 8, 9]
    # for index in index_positions:
    #    print(f"value at {index} = {numbers[index]}")


    # list of range 5 values [0, 1, 2, 3, 4]
    # index_positions = list(range(1000))
    # index_positions = list(range(len(numbers)))
    # print(f"index_positions = {index_positions}")

    # index_position = [2, 3, 4, 5]
    # stop in range will NOT include the upper bound (2, 5)
    index_positions = list(range(2, 6))
    print(f"index_positions = {index_positions}")

    # traditional for loop
    for index in index_positions:
        print(f"value at {index} = {numbers[index]}")

# function1()



def function2():
    # array of strings
    countries = ["india", "usa", "uk", "japan"]
    print(countries)
    print(f"type of countries = {type(countries)}")
    print(f"number of countries = {len(countries)}")

    for country in countries:
        print(f"country = {country}")

    print("-*-"*20)

    index_positions = list(range(len(countries)))
    print(f"index_positions = {index_positions}")

    for index in index_positions:
        print(f"value at {index} = {countries[index]}")

function2()
