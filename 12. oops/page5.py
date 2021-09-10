# Person
# - name, address, email, phone, age
# - print_info, setters, getters, can_vote, initializer
# - age must be within 20-60

class Person:
    """
    This is a Person class
    """
    def __init__(self, name, address, email, phone, age):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def set_age(self, age):
        if (age >= 20) and (age <= 60):
            self.__age = age
        else:
            print("invalid age")

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_age(self):
        return self.__age

    def print_info(self):
        print(f"name = {self.__name}")
        print(f"address = {self.__address}")
        print(f"email = {self.__email}")
        print(f"phone = {self.__phone}")
        print(f"age = {self.__age}")

    def can_vote(self):
        if self.__age >= 18:
            print(f"{self.__name} is eligible for voting")
        else:
            print(f"{self.__name} is NOT eligible for voting")

p1 = Person(name='person1', address='pune', email='person1@test.com', phone='+91234335', age=30)
p1.set_age(15)
p1.print_info()
p1.can_vote()


