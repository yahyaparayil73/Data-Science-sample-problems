import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('datasets/restaurant_dataset_100_rows.xlsx')
# print(df)
print(df.head())

# print(df.isnull().sum())

# print(df.info())

# print(df.size)

# print(df.shape)

# plt.hist(x=df['rating'])
# plt.xlabel("types of dining")
# plt.show()

sns.boxplot(x=df['online_order'],y=df['rating'])
plt.show()


