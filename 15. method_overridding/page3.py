# num
num1 = 100
num2 = 300

print(f"{num1} == {num2} = {num1 == num2}")
print(f"{num1} != {num2} = {num1 != num2}")

print(f"{num1} > {num2} = {num1 > num2}")
print(f"{num1} >= {num2} = {num1 >= num2}")

print(f"{num1} < {num2} = {num1 < num2}")
print(f"{num1} <= {num2} = {num1 <= num2}")

print(f"-" * 50)

# str
str1 = "test1"
str2 = "test2"

print(f"{str1} == {str2} = {str1 == str2}")
print(f"{str1} != {str2} = {str1 != str2}")

print(f"{str1} > {str2} = {str1 > str2}")
print(f"{str1} < {str2} = {str1 < str2}")

print(f"{str1} >= {str2} = {str1 >= str2}")
print(f"{str1} <= {str2} = {str1 <= str2}")

print(f"-" * 50)


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"Person [name: {self.__name}, age: {self.__age}]"


p1 = Person('person1', 10)
p2 = Person('person2', 20)

# p3 = p1

print(f"p1 = {p1}, type = {type(p1)}")
print(f"p2 = {p2}, type = {type(p2)}")

# print(f"p1 == p3 = {p1 == p3}")

print(f"p1 == p2 = {p1 == p2}")
print(f"p1 != p2 = {p1 != p2}")

# print(f"p1 > p2 = {p1 > p2}")
# print(f"p1 < p2 = {p1 < p2}")
