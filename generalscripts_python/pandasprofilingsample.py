import numpy as np
import pandas as pd
import pandas_profiling

df = pd.read_csv('C:\myfiles\QA\grepserpython\generalscripts_python\\flywheel\\201906271006-Amazon-com-SOV-Base-2019-06-27.csv', encoding='latin')

profile = pandas_profiling.ProfileReport(df)
df.drop(['Country', 'Client_Name', 'Business_Unit', 'Retailer', 'Brand', 'Page', 'URL', 'Rank', 'Price',
         'Absolute_Rank', 'UTCTime', 'Search_Dept_Sponsored', 'Search_Dept', 'Customer_ASIN', 'Price',
         'Zone_Name', 'Zone_ID', 'Scrape_Source', 'Search_Dept_Dropdown', 'Search_Dept_Dropdown_ID',
         'Other_Sellers_Price', 'Private_Label_Container', 'Average_Rating', 'Total_Reviews', 'Private_Label'], axis=1).head()

pd.value_counts(df['Keyword']).plot(kind='pie').invert_yaxis()
profile.to_file(output_file="output1.html")