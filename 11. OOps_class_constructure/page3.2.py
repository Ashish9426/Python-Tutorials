class Person:
    pass

def print_info(person):
    print('inside print_info')
    print(f"name: {getattr(person, 'name')}")
    print(f"age: {getattr(person, 'age')}")

def can_vote(person):
    print('inside can_vote')
    if getattr(person, 'age') >= 18:
        print(f"{getattr(person, 'name')} is eligible for voting")
    else:
        print(f"{getattr(person, 'name')} is eligible for voting")


p1 = Person()
setattr(p1, 'name','person1')
setattr(p1, 'age', 30)
print_info(p1)
can_vote(p1)

p2 = Person()
setattr(p2, 'name','person2')
setattr(p2, 'age', 10)
print_info(p2)
can_vote(p2)
