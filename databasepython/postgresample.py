import psycopg2
import json
# import re
# from json2df import series2df
# import pandas as pd
# import numpy as np


conn = psycopg2.connect(database="vericred", user = "postgres", password = "mukesh", host = "127.0.0.1", port = "5432")
#
print("Opened database successfully")
#
cur = conn.cursor()

# tablename = 'sample'

cur.execute('''CREATE TABLE michigancomplete
    (data jsonb not null);''')
print("Table created successfully")

# # appenddata = []
# # # appendall = []
# cur.execute("SELECT distinct(data) from horionnew")
# rows = cur.fetchall()
# finalval = json.dumps(rows)
# abc = json.loads(finalval)
# # # print(abc)
# #     # print(finaldata)
# #
# #
# with open('/Users/mukesh/Documents/myprojects/projectfiles/vericredprojects/horizon/horiziondeduped.json', 'w') as file:
#     for lin in abc:
#         json.dump(lin, file)
#         file.write('\n')

#
urllink = 'C:\myfiles\QA\projectfiles\\vericred_project\michigancomplete\\vericred_michigan_complete_health_20190430.json'
with open(urllink, 'r') as f:
    next(f)
    data = f
    cur.copy_from(data, 'michigancomplete', size=4096)
conn.commit()

