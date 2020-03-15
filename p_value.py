# remember to import the following
# from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import scipy as stats

def pvalue(intercept, coefficients, predictions, X, y):
    params = np.append(intercept, coefficients)

    X.insert(0, "Constant", np.ones(len(X)).tolist(), True)

    MSE = float((np.sum((y - predictions)**2)) / (len(X) - len(X.columns)))

    var_b = np.diagonal(np.linalg.inv(np.dot(X.T,X))) * MSE

    print(var_b)
    sd_b = np.sqrt(var_b)
    print(sd_b)
    ts_b = params / sd_b

    # p_values =[2*(1-stats.t.cdf(np.abs(i),(len(newX)-1))) for i in ts_b]

    # sd_b = np.round(sd_b,3)
    # ts_b = np.round(ts_b,3)
    # p_values = np.round(p_values,3)
    # params = np.round(params,4)

    # myDF3 = pd.DataFrame()
    # myDF3["Coefficients"],myDF3["Standard Errors"],myDF3["t values"],myDF3["Probabilites"] = [params,sd_b,ts_b,p_values]
    # print(myDF3)