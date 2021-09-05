# class Person(object):
# class Person():
class Person:
    pass


class Employee(Person):
    pass


class Manager(Employee):
    pass


# print(f"base class for Manager: {Manager.__base__}")
# print(f"base class for Employee: {Employee.__base__}")
# print(f"base class for Person: {Person.__base__}")

class Car(object):
    def __init__(self, model, company):
        self.__model = model
        self.__company = company

    # overriding the __str__ method
    def __str__(self):
        return f"Car [model: {self.__model}, company: {self.__company}]"


# print(f"base class for Car: {Car.__base__}")
# print(f"base class for object: {object.__base__}")

# int
# num = int(100)
num = 100
print(f"num = {num}, type = {type(num)}")
print(f"num = {num.__str__()}, type = {type(num)}")

print("-" * 50)

# str
name = "test"
print(f"name = {name}, type = {type(name)}")
print(f"name = {name.__str__()}, type = {type(name)}")

print("-" * 50)

# Car
c1 = Car('i20', 'hyundai')
print(f"c1 = {c1}, type = {type(c1)}")
print(f"c1 = {c1.__str__()}, type = {type(c1)}")
