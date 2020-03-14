import pandas as pd

data = pd.read_csv("season_stats_merged.csv")
data = data.dropna()

# print(data.head())

X = data[["Year","Pos","Age","height","weight"]]
y = data[["TS%"]]

print(X["Pos"].value_counts())

# print(X.describe())
# print("\n")
# print(X["Pos"].describe())
# print("\n")
# print(y.count())

from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(train_X, train_y)