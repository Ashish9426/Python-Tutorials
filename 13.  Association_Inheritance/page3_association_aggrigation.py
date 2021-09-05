class Address:
    def __init__(self, city, state, country):
        self.__city = city
        self.__state = state
        self.__country = country

    def print_address(self):
        print(f"city = {self.__city}")
        print(f"state = {self.__state}")
        print(f"country = {self.__country}")

class Person:
    def __init__(self, name, city, state, country, age):
        self.__name = name
        self.__age = age
        self.__address = Address(city, state, country)

    def print_info(self):
        print(f"---Person Details---")
        print(f"name = {self.__name}")
        print(f"age = {self.__age}")
        self.__address.print_address()
        print('*' * 40)

# p1 = Person('person1', 'pune', 'MH', 'india', 10)
# print(p1.__dict__)
#p1.print_info()

class House:
    def __init__(self, owner, city, state, country):
        self.__owner = owner
        self.__address = Address(city, state, country)

    def print_info(self):
        print(f"--- house details ---")
        print(f"owner = {self.__owner}")
        self.__address.print_address()
        print("-" * 40)


h1 = House('owner1', 'mumbai', 'MH', 'india')
h1.print_info()


