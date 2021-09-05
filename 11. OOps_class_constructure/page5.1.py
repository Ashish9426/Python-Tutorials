class Person:
    '''
    this class represents a person object.. blah, blah, blah..
    '''
    def print_info(self):
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"age: {self.age}")

    def can_vote(self):
        if self.age >= 18:
            print(f"{self.name} is eligible for voting")
        else:
            print(f"{self.name} is not eligible for voting")

#p1 = Person()
#p1.name = 'person1'
#p1.age = 20
#p1.address = 'pune'
#p1.print_info()
#p1.can_vote()

p2 = Person()
p2.print_info()
p2.can_vote()
# Error : AttributeError: 'Person' object has no attribute 'name'
