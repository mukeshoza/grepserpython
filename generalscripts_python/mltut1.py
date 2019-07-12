import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 50)

df = quandl.get('wiki/googl')
df = df[['Adj. Open',  'Adj. High', 'Adj. Low',  'Adj. Close',  'Adj. Volume']]
df['high_per'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['per_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close', 'high_per', 'per_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

x = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

x = preprocessing.scale(x)
y = np.array(df['label'])

