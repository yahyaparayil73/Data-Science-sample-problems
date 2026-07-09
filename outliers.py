import pandas as pd
import seaborn as sns
import matplotlib.pyplot  as plt

df = pd.DataFrame({
    "Salary":[
        30000,
        35000,
        40000,
        45000,
        50000,
        55000,
        7000000
    ]
})

sns.boxplot(x = df['Salary'])
plt.show()

Q1 = df["Salary"].quantile(0.25)

Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR

upper = Q3 + 1.5 * IQR

print("Lower Limit:", lower)
print("Upper Limit:", upper)

outliers = df[
    (df["Salary"] < lower) |
    (df["Salary"] > upper)
]

print("\nOutliers:")
print(outliers)