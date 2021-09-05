class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def print_person_info(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.age}")


class Employee(Person):
    def __init__(self, name, address, age, id, company):
        Person.__init__(self, name, address, age)
        self.id = id
        self.company = company


# object of base class
p1 = Person('person1', 'pune', 20)
#p1.print_person_info()

#object of Derived class
e1 = Employee('employee1', 'pune', 35, 1, 'company1')
e1.print_person_info()
print(e1.__dict__)
print(p1.__dict__)
