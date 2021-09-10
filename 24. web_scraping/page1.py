import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./Salary_Data.csv')
# print(df.columns)

plt.plot(df['YearsExperience'], df['Salary'], color="green", label="Salary")
plt.scatter(df['YearsExperience'], df['Salary'], color="red")

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Employee experience vs salary")

plt.legend()

plt.tight_layout()
plt.show()