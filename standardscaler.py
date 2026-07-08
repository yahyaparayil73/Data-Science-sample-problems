import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler




data = fetch_california_housing()
df = pd.DataFrame(data.data,columns=data.feature_names)
print(df)

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

print(scaled_data)


scaled_df = pd.DataFrame(scaled_data,columns = df.columns)

print(scaled_df)












