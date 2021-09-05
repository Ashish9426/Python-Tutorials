class Person:
    def __init__(self):
        self.name = ''
        self.address = ''
        self.age = 0

    def print_person_info(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.age}")


class Employee(Person):
    # derived class object getting initialized
    def __init__(self):
        # base class object getting initialized within derived class object
        Person.__init__(self)
        self.id = 0
        self.company = ''

# object of Base class
p1 = Person()
p1.print_person_info()

# object of Derived class
e1 = Employee()
#e1.print_person_info()

e2 = Employee()
#e2.print_person_info()

print(p1.__dict__)
print(e1.__dict__)
print(e2.__dict__)

