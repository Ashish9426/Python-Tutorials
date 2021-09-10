import matplotlib.pyplot as plt


def function1():
    ages = [22, 23, 25, 26, 27, 28, 29, 30, 31]
    salaries = [50, 45, 55, 65, 50, 30, 35, 70, 90]

    # line chart
    plt.plot(ages, salaries)

    # display the chart
    plt.show()


# function1()


def function2():
    ages = [22, 23, 25, 26, 27, 28, 29, 30, 31]
    salaries = [50, 45, 55, 65, 50, 30, 35, 70, 90]

    # line chart
    plt.plot(ages, salaries)
    plt.xlabel('Employee Age')
    plt.ylabel('Employee Salary in thousand')
    plt.title('Age VS Salary')

    # display the chart
    plt.show()


# function2()


def function3():
    ages = [22, 23, 25, 26, 27, 28, 29, 30, 31]
    salaries = [50, 45, 55, 65, 50, 30, 35, 70, 90]
    expenses = [10, 15, 20, 22, 25, 30, 35, 38, 39]

    # line chart
    plt.plot(ages, salaries)
    plt.plot(ages, expenses)

    plt.xlabel('Employee Age')
    plt.ylabel('Employee Salary in thousand')
    plt.title('Age VS Salary')

    # display the chart
    plt.show()


# function3()


def function4():
    ages = [22, 23, 25, 26, 27, 28, 29, 30, 31]
    salaries = [50, 45, 55, 65, 50, 30, 35, 70, 90]
    expenses = [10, 15, 20, 22, 25, 30, 35, 38, 39]

    # line chart
    plt.plot(ages, salaries, color="green", label="salaries")
    plt.plot(ages, expenses, color="red", label="expenses")

    # point chart
    plt.scatter(ages, salaries, color="green")
    plt.scatter(ages, expenses, color="red")

    # add title and labels
    plt.xlabel('Employee Age')
    plt.ylabel('Employee Salary in thousand')
    plt.title('Age VS Salary')

    # show legend
    plt.legend()

    # display the chart with equal spacing around all borders
    plt.tight_layout()

    # save the graph as a file
    plt.savefig('./charts/age_vs_salary_vs_expense.png')

    # display the chart
    # plt.show()


# function4()


def function5():
    marks = [60, 80, 60, 45, 70]
    subjects = ["Maths", "Computer", "Science", "Language", "Biology"]
    explodes = [0, 0.1, 0, 0, 0]

    plt.pie(marks, labels=subjects, shadow=True, explode=explodes, autopct='%1.1f%%')
    plt.tight_layout()
    plt.savefig('./charts/student_marks.png')
    plt.show()


function5()
