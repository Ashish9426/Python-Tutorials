class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def print_person_info(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.age}")


# p1 = Person('person1', 'pune', 20)
# p1.print_info()


class Employee:
    def __init__(self, name, address, age, company_name, salary):
        self.name = name
        self.address = address
        self.age = age
        self.company_name = company_name
        self.salary = salary

    def print_employee_info(self):
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"age: {self.age}")
        print(f"company_name: {self.company_name}")
        print(f"salary: {self.salary}")


e1 = Employee('employee 1', 'pune', 45, 'company1', 10.50)
e1.print_employee_info()
