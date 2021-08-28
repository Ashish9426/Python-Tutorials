def can_vote(person):
    if person["age"] >= 18:
        print(f"yes. {person['name']} is eligible for voting")
    else:
        print(f"no. {person['name']} is NOT eligible for voting")


# person1 data
person1 = {
    "name": "person1",
    "address": "pune",
    "phone": "+913533455",
    "email": "person1@test.com",
    "age": 10
}

# person2 data
person2 = {
    "name": "person2",
    "address": "mumbai",
    "phone": "+913533456",
    "email": "person2@test.com",
    "age": 20
}


can_vote(person1)
can_vote(person2)
can_vote(10)
