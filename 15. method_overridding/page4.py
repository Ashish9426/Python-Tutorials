class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"Person [name: {self.__name}, age: {self.__age}]"

    def __gt__(self, other):
        # check if the age of person1 is greater than person2's age
        return self.__age > other.__age

    def __lt__(self, other):
        # check if the age of person1 is less than person2's age
        return self.__age < other.__age

    def __ge__(self, other):
        # check if the age of person1 is greater than or equals to person2's age
        return self.__age >= other.__age

    def __le__(self, other):
        # check if the age of person1 is less than or equals to person2's age
        return self.__age <= other.__age

    def __eq__(self, other):
        # check of both the persons are having same name and age
        return (self.__name == other.__name) and (self.__age == other.__age)

    def can_vote(self):
        return self.__age >= 18


num1 = 100
num2 = 300

print(f"{num1} == {num2} = {num1 == num2}")
print(f"{num1} == {num2} = {num1.__eq__(num2)}")

print(f"{num1} > {num2} = {num1 > num2}")
print(f"{num1} > {num2} = {num1.__gt__(num2)}")

print('-' * 80)

str1 = "test1"
str2 = "test2"

print(f"{str1} == {str2} = {str1 == str2}")
print(f"{str1} == {str2} = {str1.__eq__(str2)}")

print(f"{str1} > {str2} = {str1 > str2}")
print(f"{str1} > {str2} = {str1.__gt__(str2)}")

print('-' * 80)

p1 = Person('person1', 10)
p2 = Person('person2', 20)

# Person.can_vote(p1)
# p1.can_vote()

print(f"p1 == p2 = {p1 == p2}")
print(f"p1 == p2 = {p1.__eq__(p2)}")

print(f"p1 > p2 = {p1 > p2}")
# print(f"p1 > p2 = {p1.__gt__(p2)}")

print(f"p1 < p2 = {p1 < p2}")
# print(f"p1 < p2 = {p1.__lt__(p2)}")

print(f"p1 >= p2 = {p1 >= p2}")
# print(f"p1 >= p2 = {p1.__ge__(p2)}")

print(f"p1 <= p2 = {p1 <= p2}")
#print(f"p1 <= p2 = {p1.__le__(p2)}")
