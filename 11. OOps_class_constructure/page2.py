# empty class
class Person:
    pass

# instantation: creating an object of a class
# reference object
person = Person()

# object
# - collection of key-value pairs
# - keys => attributes
print(person.__dict__)

# add new attribute
setattr(person, 'name','person1')
setattr(person, 'address' ,'pune')
setattr(person, 'age', 40)

print(person.__dict__)

# getting value of an attribute name
print("name=",getattr(person, 'name'))
print("address=",getattr(person, 'address'))
print("age=",getattr(person, 'age'))

# create another object
person2 = Person()
print(person2.__dict__)

setattr(person2, "first_name", "person2")
setattr(person2, "full_address", "mumbai")
setattr(person2, "person_age", 10)
setattr(person2, "email", "person2@test.com")
setattr(person2, "mobile", "+91344565")

print(person2.__dict__)

print(f"name = {getattr(person2, 'first_name')}")
print(f"address = {getattr(person2, 'full_address')}")
print(f"age = {getattr(person2, 'person_age')}")
print(f"email ={getattr(person2, 'email')}")
print(f"mobile ={getattr(person2, 'mobile')}")



