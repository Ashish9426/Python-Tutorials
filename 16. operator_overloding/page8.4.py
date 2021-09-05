class Employee:
    def __init__(self, name, employee_id):
        self.__name = name
        self.__employee_id = employee_id

    def __str__(self):
        return f"Employee [id: {self.__employee_id}, name: {self.__name}]"


class Company:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__index = 0
        # list of employees
        self.__employees = []

    def print_info(self):
        print("-" * 80)
        print(f"name: {self.__name}")
        print(f"-- employee list --")
        for employee in self.__employees:
            print(employee)
        print(f"-- employee list --")
        print("-" * 80)

    def add_employee(self, name, id):
        employee = Employee(name, id)
        self.__employees.append(employee)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__employees):
            employee = self.__employees[self.__index]
            self.__index += 1
            return employee
        else:
            raise StopIteration()


# e1 = Employee('employee 1', 1)
# print(e1)

c1 = Company('company 1', 'pune')
c1.add_employee('employee 1', 1)
c1.add_employee('employee 2', 2)
c1.add_employee('employee 3', 3)
c1.add_employee('employee 4', 4)
#c1.print_info()

for employee in c1:
    print(employee)

# iterator = c1.__iter__()
# iterator = iter(c1)
# print(iterator)

# iterator.__next__()
# try:
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
# except:
#     print("end of company employee list")
