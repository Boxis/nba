import pandas as pd

data = pd.read_csv("season_stats_merged.csv")
data = data.dropna()
data = data[data.Year >= 1968]
data = data[data.Tm != "TOT"]
data["g_norm"] = data["G"] / 82
data = data[~data.Pos.isin(["F", "G", "F-C", "C-F", "G-F", "F-G"])]

print(data.head())

X = data[["Year","Pos","Age","height","weight","g_norm"]]
y = data[["TS%"]]

# print(X["Pos"].value_counts())

# print(X.describe())
# print("\n")
# print(X["Pos"].describe())
# print("\n")
# print(y.count())

from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y)
weight = train_X["g_norm"]
train_X.drop("g_norm",axis=1)

object_cols = ["Pos"]

dummies_train = pd.get_dummies(train_X.Pos, prefix="Pos")
dummies_val = pd.get_dummies(val_X.Pos, prefix="Pos")

num_train_X = train_X.drop(object_cols, axis=1)
num_val_X = val_X.drop(object_cols, axis=1)

OH_train_X = pd.concat([num_train_X, dummies_train], axis = 1)
OH_val_X = pd.concat([num_val_X, dummies_val], axis = 1)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(OH_train_X, train_y,sample_weight=weight)

print(model.coef_)
preds = model.predict(OH_val_X)

from sklearn.metrics import mean_absolute_error

print(mean_absolute_error(val_y,preds))