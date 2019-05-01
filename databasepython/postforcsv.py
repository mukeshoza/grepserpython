import psycopg2
import json
from json2df import series2df
import pandas as pd
import numpy as np


conn = psycopg2.connect(database="test", user = "postgres", password = "mukesh", host = "127.0.0.1", port = "5432")
#
print("Opened database successfully")
#
cur = conn.cursor()

# tablename = 'sample'

cur.execute('''CREATE TABLE floridachild
       (ProviderName text,
       ProviderType text not null,
       Address text,
       phonenumber text,
       Licensenumber text,
       Capacity	text,
       Status text,
       Expiration text,
       FaithBased text,
       HeadStart text,
       SchoolReadiness text,
       OperationTime text,
       Programs text,
       Services text,
       URL text
       );''')
print("Table created successfully")

# appenddata = []
# appendall = []
# cur.execute("SELECT distinct(data) from samplejson")
# rows = cur.fetchall()
# finalval = json.dumps(rows, sort_keys=True)
# ab = json.loads(finalval)
#
# with open('/Users/mukesh/Documents/myprojects/projectfiles/vericredprojects/samplededup.json', 'w') as file:
#     for lin in ab:
#         json.dump(lin, file)
#         file.write('\n')


urllink = '/Users/mukesh/Documents/myprojects/projectfiles/floridachild/201903131227-Florida_Child_Care2019-03-13.csv'
with open(urllink, 'r', encoding='latin-1') as f:
    next(f)
    data = f
    cur.copy_from(data, 'floridachild', size=4096)
conn.commit()
