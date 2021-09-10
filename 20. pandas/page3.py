import pandas as pd
import numpy as np


def function1():
    df = pd.read_csv('./Salary_Data.csv')
    print(df)
    print("-" * 80)
    print(df.info())
    print("-" * 80)
    print(df.describe())
    print("-" * 80)
    print(df.head(4))
    print("-" * 80)
    print(df.tail(4))


# function1()


def function2():
    df = pd.read_csv('./Salary_Data.csv')
    print("-" * 80)
    print(df.head(4))
    print("-" * 80)

    # indexing

    # select YearsExperience from salary_data
    # print(df['YearsExperience'])

    # select Salary from salary_data
    # print(df['Salary'])
    print(f"type = {type(df['Salary'])}")

    # select YearsExperience, Salary from salary_data
    # print(df[['YearsExperience', 'Salary']])

    # get a specific row
    # select YearsExperience from salary_data where index = 2
    # print(f"exp at 2 position = {df['YearsExperience'][2]}")

    # select Salary from salary_data where index = 2
    print(f"salary at 2 position = {df['Salary'][2]}, type = {type(df['Salary'][2])}")

    # select YearsExperience, Salary from salary_data = 2
    # print(f"type = {type(df[['YearsExperience', 'Salary']])}")


# function2()


def function3():
    df = pd.read_csv('./Salary_Data.csv')
    print("-" * 80)
    print(df.head(4))
    print("-" * 80)

    # filtering
    # print(df['Salary'] > 60000)

    # select * from salary_data where Salary > 60000
    # print(df[df['Salary'] > 60000])

    # select * from salary_data where YearsExperience >= 3
    # print(df[df['YearsExperience'] >= 3])

    # select YearsExperience from salary_data where Salary > 60000
    # print(df[df['Salary'] > 60000]['YearsExperience'])

    # select Salary from salary_data where YearsExperience >= 5
    print(df[df['YearsExperience'] >= 5]['Salary'])


# function3()


def function4():
    df = pd.read_csv('./Salary_Data.csv')
    print(df.columns)

    # adding a column
    df['Bonus'] = df['Salary'] * 0.10

    print(df.columns)

    print("-" * 80)
    print(df.head(5))
    print("-" * 80)

    # write the changes to the new csv file
    df.to_csv('./Salary_Data.csv')


# function4()


def function5():
    df = pd.read_csv('./Wine.csv')
    print(df.columns)

    # print(df.head())
    # print(f"-" * 80)
    # print(df.info())
    # print(f"-" * 80)
    # print(df.describe())
    # print(f"-" * 80)

    # drop a column
    del df['Alcohol']
    del df['Malic_Acid']

    # drop columns
    df_new = df.drop(['Ash', 'Ash_Alcanity', 'Magnesium', 'Total_Phenols'], axis=1)

    print(df.columns)
    print(df_new.columns)


function5()
