import pandas as pd
import numpy as np


def function1():
    df = pd.read_csv('./Salary_Data.csv')

    print("-" * 80)
    print(df.head(4))
    print("-" * 80)

    # print(df['Salary'][0])
    # print(df.iloc[0, 1])
    #
    # print(df['YearsExperience'][3])
    # print(df.iloc[3, 0])

    # print(df[df['Salary'] > 60000])
    # print(df.iloc[:, :][df.Salary > 60000])

    # select YearsExperience from salary_data where salary > 60000
    print(df.iloc[:, 0][df.Salary > 60000])


function1()


def function2():
    df = pd.read_csv('./Wine.csv')

    print(df.head())
    # print(df[['Alcohol', 'Malic_Acid', 'Ash']])
    # print(df.iloc[:, 0:3])
    # print(df.iloc[:, :3])
    # print(df.iloc[:10, :3])

# function2()
