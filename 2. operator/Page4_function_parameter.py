def function1(param):
    # param = 10
    print("inside function1")
    print(f"param = {param}, type = {type(param)}")

# function1(10)
# function1(param = 10)

def function2(p1, p2):
    print("inside function2")
    print(f"p1 = {p1}, type = {type(p1)}")
    print(f"p2 = {p2}, type = {type(p2)}")

# function2(20, 30)
# function2(p1=20, p2=30)
# function2(p2=30, p1=20)
# function2(30, 20)


def function3(p1, p2, p3, p4):
    print("inside function 3")
    print(f"p1 = {p1}, type = {type(p1)}")
    print(f"p2 = {p2}, type = {type(p2)}")
    print(f"p3 = {p3}, type = {type(p3)}")
    print(f"p4 = {p4}, type = {type(p4)}")

# function3(10,20,30,40)
# function3(p1=30,p4=10)

# print("enter value 1:")
# value1 = input()

# print("enter value 2:")
# value2 = input()

# print("enter value 3:")
# value3 = input()

# print("enter value 4:")
#value4 = input()

#function3(value1,value2,value3,value4)




def function4(p1, p2=20):
    print("inside function 4")
    print(f"p1 = {p1}, type = {type(p1)}")
    print(f"p2 = {p2}, type = {type(p2)}")


# function4(10, 20)
# function4(10)
# function4(40, 60)
# function4(p1=40, p2=60)
# function4(p1=50)


def function5(p1, p2, p3=30, p4=None):
    print("inside function 4")
    print(f"p1 = {p1}, type = {type(p1)}")
    print(f"p2 = {p2}, type = {type(p2)}")
    print(f"p3 = {p3}, type = {type(p3)}")
    print(f"p4 = {p4}, type = {type(p4)}")


# function5(p1=10, p2=20)
# function5(p3=90, p4=100, p2=80, p1=90)
