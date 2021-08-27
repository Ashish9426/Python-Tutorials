def can_vote(age):
    """
    this function is made to check if a person is eligible for voting
    :param age: age of a person
    :return: nothing
    """

    if age >= 18:
        print(f"this person is eligible for vote")
    else:
        print(f"this person can not vote")

age_1 = 18
can_vote(age_1)

print("-*-" * 20)

age_2 = 10
can_vote(age_2)

print("-*-" * 20)

age_3 = 50
can_vote(age_3)