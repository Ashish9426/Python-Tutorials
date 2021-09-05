class Person:
    """
    this is a test person class
    """
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_info(self):
        print(f"name = {self.__name}")
        print(f"age = {self.__age}")

    def can_vote(self):
        return self.__age >= 18


class Employee:
    pass


class Player:
    pass


class Student:
    pass

# execute the following code only when
# page1 is the main module
if __name__ == "__main__":
    print(f"page1 module name: {__name__}")
    person = Person('person1', 10)
    person.print_info()
    print(f"can vote = {person.can_vote()}")
