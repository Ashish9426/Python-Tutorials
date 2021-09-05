class Person:
    pass

p1 = Person()
setattr(p1, 'name','person1')
setattr(p1, 'age', 30)

print(f"name: {getattr(p1, 'name')}")
print(f"age: {getattr(p1, 'age')}")

if getattr(p1, 'age') >= 18:
    print(f"{getattr(p1, 'name')} is eligible for voting")
else:
    print(f"{getattr(p1, 'name')} is eligible for voting")

p2 = Person()
setattr(p2, 'name','person2')
setattr(p2, 'age', 10)

print(f"name: {getattr(p2, 'name')}")
print(f"age: {getattr(p2, 'age')}")


if getattr(p2, 'age') >= 18:
    print(f"{getattr(p2, 'name')} is eligible for voting")
else:
    print(f"{getattr(p2, 'name')} is eligible for voting")


