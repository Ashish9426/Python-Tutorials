def function1():
    # empty list
    l1 = []
    print(f"l1 = {l1}, type = {type(l1)}")

    # empty list
    l2 = list()
    print(f"l2 = {l2}, type = {type(l2)}")

    # empty tuple
    t1 = ()
    print(f"t1 = {t1}, type = {type(t1)}")

    # empty tuple
    t2 = tuple()
    print(f"t2 = {t2}, type = {type(t2)}")

    # empty set
    s1 = set()
    print(f"s1 = {s1}, type = {type(s1)}")

    # empty set
    s3 = {10,20,30}
    print(f"s3 = {s3}, type = {type(s3)}")

    # empty fozenset
    s2 = frozenset()
    print(f"s2 = {s2}, type = {type(s2)}")

    # empty dictionary
    d1 = {}
    print(f"d1 = {d1}, type = {type(d1)}")

    # empty dictionary
    d2 = dict()
    print(f"d2 = {d2}, type = {type(d2)}")

# function1()

def function2():
    name1 = 'person1'
    address1 = 'allahabad'
    email1 = 'ashishm26s94@gmail.com'

    name2 = 'person2'
    address2 = 'lucknow'
    email2 = 'person2@gmail.com'

    # list
    person1 = ["person1","allahabad","ashishm26s94@gmail.com"]
    person2 = ["person2","lucknow","person2@gmail.com"]

    # set
    person1 = {"person1", "allahabad", "ashishm26s94@gmail.com"}
    person2 = {"person2", "lucknow", "person2@gmail.com"}

    # tuple
    person1 = ("person1", "allahabad", "ashishm26s94@gmail.com")
    person2 = ("person2", "lucknow", "person2@gmail.com")

    print(f"name = {person1[0]}")
    print(f"address1 = {person1[1]}")
    print(f"email = {person1[2]}")

    print("-*-" * 20)

    print(f"name = {person2[0]}")
    print(f"address2 = {person2[1]}")
    print(f"email = {person2[2]}")

# function2()

def function3():
    # dictionary
    # collection of key-value pairs
    person1 = {"name": "person1", "address": "pune", "email": "person1@test.com"}
    print(f"person1 = {person1}, type = {type(person1)}")

    # the second email will be kept
    person2 = {"address": "mumbai", "name": "person2", "email": "person2@test.com", "email": "person3@test.com"}
    print(f"person2 = {person2}, type = {type(person2)}")

    print(f"name = {person1['name']}")
    print(f"address = {person1['address']}")
    print(f"email = {person1['email']}")
    print("-" * 20)
    print(f"name = {person2['name']}")
    print(f"address = {person2['address']}")
    print(f"email = {person2['email']}")

    print("-" * 20)
    print("-" * 20)

    print(f"keys = {person1.keys()}")
    print(f"values = {person1.values()}")

# function3()

def function4():
    person1 = {
        "name": "person1",
        "age": 40,
        "salary": 10.50,
        "address": {
            "city": "pune",
            "state": "MH",
            "country": "india",
            "pin code": 21207
        },
        "CanVote": True,
        "email":[
            "person1@home.com",
            "person1@company.com",
            "person1@special.com"
        ]
    }
    # print(f"name: {person1['name']}")
    # print(f"age: {person1['age']}")
    # print(f"address: {person1['address']}")
    print(f"address: {person1['address']['city']}, {person1['address']['state']}, {person1['address']['country']}")
    print(f"home email = {person1['email'][0]}")
    print(f"company email = {person1['email'][1]}")
    print(f"special email = {person1['email'][2]}")

    print(f"-" * 20)

    keys = person1.keys()
    for key in keys:
        print(f"{key} = {person1[key]}")


# function4()

def function5():
    d1 = {'k1': 'v1', 'k2': 'v2'}
    d2 = {}

    for key in d1.keys():
        value = d1[key]
        d2[value] = key

    print(d1)
    print(d2)


# function5()

def function6():
    person = {}

    print("enter name:")
    person['name'] = input()

    print("enter address:")
    person['address'] = input()

    print("Enter email id")
    person['email id'] = input()

    print(person)


function6()




