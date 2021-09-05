class Person:
    '''
    this class represents a person object.. blah, blah, blah..
    '''
    def __init__(self):
        '''
        initializer method
        - gets called automatically for every object of this class
        - similar to constructor
        '''
        print('inside __init__')
        self.name = ''
        self.address = ''
        self.age = 0

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

p3 = Person()
p4 = Person()