# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:45:45 2020

@author: Boxi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = pd.read_csv("season_stats_merged.csv")
data.shape

data.describe()

data.isnull().any()

# drop all NA values
cleaned = data.dropna()
cleaned.isnull().any()

X = cleaned[['Year', 'Age', 'height', 'weight']]
y = cleaned['TS%'].values

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(cleaned['TS%'])
# most TS% around 0.5

# split data into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=0)

# train model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
coeff_df

# predictions on test data
y_pred = regressor.predict(X_test)

# difference between actual & predicted value
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)
df1

# plot comparison of Actual vs Predicted values
df1.plot(kind='bar', figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

# evaluate performance by looking at MAE, MSE, RMSE
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

y.mean()
