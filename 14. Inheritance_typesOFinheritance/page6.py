class Person:
    def __init__(self, name, address, age):
        # protected
        self._name = name
        self._address = address
        self._age = age

    def print_person_info(self):
        print(f"name = {self._name}")
        print(f"address = {self._address}")
        print(f"age = {self._age}")


# Player is derived from Person class
class Player(Person):
    def __init__(self, name, address, age, team):
        Person.__init__(self, name, address, age)
        self._team = team

    def print_player_info(self):
        Person.print_person_info(self)
        print(f"team = {self._team}")


# base class object
person1 = Person('person1', 'pune', 10)
person1.print_person_info()

# derived class object
player1 = Player('player1', 'mumbai', 20, 'india')
player1.print_player_info()
#player1.print_person_info()
#player1.test_method()
