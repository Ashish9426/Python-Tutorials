class Person:
    def __init__(self, name, city, state, country, age):
        self.__name = name
        self.__city = city
        self.__state = state
        self.__country = country
        self.__age = age

    def print_info(self):
        print(f"--- person details ---")
        print(f"name = {self.__name}")
        print(f"age = {self.__age}")
        print(f"city = {self.__city}")
        print(f"state = {self.__state}")
        print(f"country = {self.__country}")
        print("-" * 40)


p1 = Person('person1', 'pune', 'MH', 'india', 10)
p1.print_info()


class House:
    def __init__(self, owner, city, state, country):
        self.__owner = owner
        self.__city = city
        self.__state = state
        self.__country = country

    def print_info(self):
        print(f"--- house details ---")
        print(f"owner = {self.__owner}")
        print(f"city = {self.__city}")
        print(f"state = {self.__state}")
        print(f"country = {self.__country}")
        print("-" * 40)


h1 = House('owner1', 'mumbai', 'MH', 'india')
h1.print_info()
