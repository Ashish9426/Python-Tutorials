class Employee:
    def __init__(self, name, employee_id):
        self.__name = name
        self.__employee_id = employee_id

    def __str__(self):
        return f"Employee [id: {self.__employee_id}, name: {self.__name}]"


e1 = Employee('employee 1', 1)
print(e1)