import pandas as pd

one_hot_data = pd.DataFrame(columns=data['whoAmI'].unique())

for value in data['whoAmI'].unique():
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

one_hot_data.head()

#Этот код работает без "get_dummies".