class Person:
    def __init__(self, name):
        self._name = name

class Employee(Person):
    def __init__(self, name, company):
        Person.__init__(self, name)
        self._company = company

class Manager(Employee):
     def __init__(self, name, company, department):
         Employee.__init__(self, name, company)
         self.department = department


p1 = Person('person1')
print(p1.__dict__)
e1 = Employee('employee1', 'company1')
print(e1.__dict__)
m1 = Manager('manager1', 'company1', 'computer')
print(m1.__dict__)
