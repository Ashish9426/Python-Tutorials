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

# function alias
# my_function = print_info


p1 = Person()
setattr(p1, 'name','person1')
setattr(p1, 'age', 30)

# function alias
setattr(p1, 'print_info', print_info)
setattr(p1, 'can_vote', can_vote)

print(p1.__dict__)

# print(f"print_info: {getattr(p1, 'print_info')}")
# function = getattr(p1, 'print_info')
# function(p1)

# print(f"name: {getattr(p1, 'name')}")
# print(f"name: {p1.name}")
# print(f"age: {p1.age}")
p1.print_info(p1)
# p1.can_vote(p1)

#print_info(p1)
#can_vote(p1)

p2 = Person()
setattr(p2, 'name','person2')
setattr(p2, 'age', 10)

# function alias
setattr(p2, 'print_info', print_info)
setattr(p2, 'can_vote', can_vote)

print(p2.__dict__)
# print(f"print_info: {getattr(p2, 'print_info')}")

# function = getattr(p2, 'print_info')
# function(p2)

print(f"name: {p2.name}")
print(f"age: {p2.age}")
p2.print_info(p2)
p2.can_vote(p2)

#print_info(p2)
#can_vote(p2)


p3 = Person()
p3.name = 'person3'
p3.age = '35'
p3.print_info = print_info
setattr(p3, "can_vote", can_vote)
setattr(p3, 'address', 'pune')

# print(p3.__dict__)
print(f"name: {p3.name}")
print(f"age: {p3.age}")
print(f"address: {p3.address}")

p3.print_info(p3)
p3.can_vote(p3)

