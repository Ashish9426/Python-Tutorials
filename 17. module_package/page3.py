def function1():
    import page1
    import car

    person1 = page1.Person('person1', 49)
    person1.print_info()

    car1 = car.Car('model1', 'company1', 0)
    car1.print_info()


# function1()


def function2():
    # p1 here is an alias of page1
    import page1 as p1
    import car as c1

    person1 = p1.Person('person1', 30)
    person1.print_info()
    print(f"can vote = {person1.can_vote()}")

    e1 = p1.Employee()

    car1 = c1.Car('fabia', 'Skoda', 5.5)
    car1.print_info()


# function2()


def function3():
    # import only Person class
    # from page1 import Person
    # from page1 import Student
    from page1 import Person, Student
    from car import Car

    st1 = Student()

    person1 = Person('person1', 40)
    person1.print_info()

    car1 = Car('model1', 'company1', 0)
    car1.print_info()


# function3()

class Person:
    def __init__(self, name):
        self.__name = name

    def print_info(self):
        print("from page3 Person")


def function4():
    # MyPerson is an alias to Person
    from page1 import Person as MyPerson
    p2 = Person('person2')
    p2.print_info()

    p1 = MyPerson('person1', 20)
    p1.print_info()


# function4()


def function5():
    # import all entities from page1
    from page1 import *
    p2 = Student()

    import page1
    p1 = page1.Student()

#function5()


def function6():
    import sunbeam.faculty
    f1 = sunbeam.faculty.Faculty()

    import sunbeam.account.accountant
    a2 = sunbeam.account.accountant.Accountant()

    # import sunbeam.account.accountant as act
    # a1 = act.Accountant

    import quiz.question
    q1 = quiz.question.Question()

    import quiz.answer as ans
    a1 = ans.Answer()

    from quiz.answer import Answer
    a2 = Answer()

#function6()
