class Person:
    def __init__(self):
        self.name = ''
        self.address = ''
        self.age = 0



# Employee is-a Person
# Employee is inherited from Person
# Employee is derived from Person
# derived class

class Employee(Person):
    pass


print(f"base class of employee: {Employee.__base__}")

p1 = Person()
print(f"p1 = {p1.__dict__}")

e1 = Employee()
print(f"e1 = {e1.__dict__}")