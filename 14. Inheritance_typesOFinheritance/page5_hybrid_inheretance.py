class Person:
    def __init__(self, name):
        self._name = name


class Player(Person):
    def __init__(self, name, team, sport):
        Person.__init__(self, name)
        self._team = team
        self._sport = sport


class CricketPlayer(Player):
    def __init__(self, name, team):
        Player.__init__(self, name, team, 'Cricket')


class Employee(Person):
    def __init__(self, name, company):
        Person.__init__(self, name)
        self._company = company


class Manager(Employee):
    def __init__(self, name, company, department):
        Employee.__init__(self, name, company)
        self._department = department


class SalesManager(Manager):
    def __init__(self, name, company, department, target):
        Manager.__init__(self, name, company, department)
        self._target = target
