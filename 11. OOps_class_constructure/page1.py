def can_vote(person):
    if person['age']>=18:
        print('yes')
    else:
        print('No')

def print_info(person):
    print('name:', person['name'])
    print('age:', person['age'])


# data
person1 = {'name':'person1', 'age':30}
can_vote(person1)
print_info(person1)

# data
mobile = {'model':'iphone', 'company':'Apple'}
can_vote(mobile)

