import pandas as pd

df = pd.read_csv('feb.csv', low_memory=False)
df2 = pd.read_csv('may.csv', low_memory=False)

df['month'] = 'Feb'
df2['month'] = 'May'

df = df.append(df2)

grpby = df.groupby(['Manufacturer', 'month'])['Country'].count().reset_index().to_csv('sample.csv')

