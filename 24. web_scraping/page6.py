import re


def function1():
    str = "this is a sampl text"
    result = re.search('sample', str)
    if result:
        print("sample word found in str")
    else:
        print("NO, sample word not found in str")


# function1()


def function2():
    password = "Test$1234"
    is_valid_password = True

    # upper case
    # print(f"is upper case letter present = {re.match('[A-Z]+', password)}")

    # lower case
    # print(f"is lower case letter present = {re.match('[a-zA-Z0-9]*[a-z]+', password)}")

    # at least one digit
    # print(f"is digit present = {re.match('[0-9]+', password)}")

    # ar least special character
    print(f"is special character present = {re.match('[a-zA-Z0-9]*[_@!#$^&*]+', password)}")

    # if is_valid_password:
    #     print("Valid password")
    # else:
    #     print("Invalid password")


function2()

