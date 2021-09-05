class Person:
    def __init__(self, name, address, age):
        self.__name  = name
        self.__address = address
        self.__age = age

    def print_info(self):
        print(f"name = {self.__name}")
        print(f"address = {self.__address}")
        print(f"age = {self.__age}")

# Person.__init__(p1, name='person1', address='address')
p1 = Person(name='person1', address='pune', age=20)

# Person.print_info(p1)
p1.print_info()

# Person.__init__(p2, name='person2', address='mumbai', age=30)
p2 = Person(name='person2', address='mumbai', age=30)

# Person.print_info(p2)
p2.print_info()


class Car:
    def __init__(self, model, company, price):
        self.model = model
        self.company = company
        self.price = price


# internal (not for developer) code conversion
# Car.__init__(i10, 'i10', 'hyundai', 5.5)
i10 = Car('i10', 'hyundai', 5.5)
