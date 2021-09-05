class Number:
    def __init__(self, num):
        self.__num = num

    # overloading > operator
    def __gt__(self, other):
        return self.__num > other.__num

    # overloading plus operator
    def __add__(self, other):
        return Number(self.__num + other.__num)

    # string conversion
    def __str__(self):
        return f"Number [{self.__num}]"


n1 = Number(10)
n2 = Number(20)
addition = n1 + n2
print(f"addition = {addition}, type = {type(addition)}")
