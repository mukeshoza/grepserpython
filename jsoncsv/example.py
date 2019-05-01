import pandas as pd
import ast
from json2df import series2df

pd.set_option('display.max_rows', 1200)
pd.set_option('display.max_columns', 5)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 50)

# jsonfile = pd.read_json('/Users/mukesh/Documents/myprojects/projectfiles/vericredprojects/vericred_health_first/vericred_healthfirst_20181228.json', lines=True)
# jsonfile.to_csv('/Users/mukesh/Documents/myprojects/projectfiles/vericredprojects/aetna/samplecsvjson.csv', index=False)

df = pd.read_csv('/Users/mukesh/Documents/myprojects/projectfiles/vericredprojects/aetna/samplecsvjson.csv', delimiter=',')

row1 = df['addresses']
row2 = df['provider']
row3 = df['specialties']

# first_row = df['provider'].head()[0]
# # print(type(first_row))
#
# abc = ast.literal_eval(first_row)
# print(abc)


extract_df = series2df(row2)
abc = df.groupby(extract_df['site_uid']).size()
if abc > 1:
    print(abc)
# replvalue = extract_df.replace(regex="\[\{'\w+|:\s+|\}\]|'|\}|\{|name", value='')
# df['city'] = replvalue
# print(df['city'])
# replvalue.to_csv('/Users/mukesh/Documents/myprojects/projectfiles/vericredprojects/samplecsv.csv', index=False)
# # extract_df1 = series2df(df['provider'])
# #
# finaldata = extract_df
# abc = finaldata
# revalue = extract_df.replace(regex='\w+\W+:|\[\{\'|\"|\}\]|\}|\{', value='|')





# print((finaldata))
#
# #
# # print(extract_df.shape)
# print(finaldata.head())
#
# revalue.to_csv('/Users/mukesh/Documents/myprojects/projectfiles/vericredprojects/aetna/sampleaddressnew.csv',
#                index=False, sep='|')
