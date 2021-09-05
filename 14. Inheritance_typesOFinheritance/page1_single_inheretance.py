# access specifiers
# - public
#   - no underscore
#   - can be accessed outside the class
# - private
#   - double underscore
#   - can be accessed only within the same class
# - protected
#   - single underscore
#   - can be accessed within same class as well as derived class

# base
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

# player is derived from person class
class Player(Person):
    def __init__(self, name, address, age, team):
        Person.__init__(self, name, address, age)
        self._team = team

    def print_player_info(self):
        print(f"name = {self._name}")
        print(f"address = {self._address}")
        print(f"age = {self._age}")
        print(f"team = {self._team}")

# base class object
person1 = Person('person1', 'pune', 10)
person1.print_person_info()
#print(person1.__dict__)

# derived class object
player1 = Player('player1', 'mumbai', 20, 'india')
player1.print_player_info()
#print(player1.__dict__)

