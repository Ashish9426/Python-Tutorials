class InvalidAgeError(Exception):
    pass


class InvalidSalaryError(Exception):
    pass


def get_user_input():
    print("Enter name: ")
    name = input()

    print("Enter age: ")
    age = input()

    #print(f"Name = {name}")
    #print(f"Age = {age}")

    # convert the string to int
    age = int(age)
    if (age < 0) or (age > 100):
        # raise an exception
        raise InvalidAgeError()

    print("enter salary: ")
    salary = input()

    # convert string to int
    salary = int(salary)
    if salary > 10000:
        raise InvalidSalaryError()

    print(f"name = {name}")
    print(f"age = {age}")
    print(f"salary = {salary}")


try:
    get_user_input()
except InvalidAgeError:
    print("age exception raised")
except InvalidSalaryError:
    print("salary exception raised")
except:
    print("generic exception raised")
