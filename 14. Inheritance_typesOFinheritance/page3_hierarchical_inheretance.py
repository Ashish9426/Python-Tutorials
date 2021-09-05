class Person:
    def __init__(self, name):
        self._name = name


class Player(Person):
    def __init__(self, name, team):
        Person.__init__(self, name)
        self._team = team


class Employee(Person):
    def __init__(self, name, company):
        Person.__init__(self, name)
        self._company = company


class Student(Person):
    def __init__(self, name, school):
        Person.__init__(self, name)
        self._school = school
