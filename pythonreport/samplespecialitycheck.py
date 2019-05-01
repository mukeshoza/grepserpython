import psycopg2 as ps
import json
import pandas as pd
import re
from tabulate import tabulate

pd.set_option('display.max_rows', 1200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1500)
pd.set_option('max_colwidth', 50)
pd.options.display.max_colwidth = 20000

conn = ps.connect(database="vericred", user="postgres", password="mukesh", host="127.0.0.1", port="5432")
cur = conn.cursor()

specappend = []
missingspec = []

cur.execute("select tablename from pg_tables where schemaname = 'public'")
tbname = cur.fetchall()
print('===================================')
print('Table Names:')
print('===================================')
for tnames in tbname:
    retname = re.sub("^\('|\'\,\)$", '', str(tnames))
    print(retname)
print('\n')
tablename1 = input('Enter tablename: ')
cur.execute("SELECT distinct(data->'addresses') from public.{}".format(tablename1))
rows = cur.fetchall()
for lines in rows:
    data = json.dumps(lines, sort_keys=False)
    readjson = json.loads(data)
    # for zips in readjson:
    #     try:
    #         print(zips[0]['state'])
    #     except:
    #         continue
# cur.execute("select count(distinct(data)) from public.{}".format((tablename1)))
# datas = cur.fetchall()
# # print(datas)
# cur.execute("select count((data)) from public.{}".format((tablename1)))
# counttotal = cur.fetchall()

    #     try:
    #         speciality = add['specialties'][0]['name']
    #         specappend.append(speciality)
    #     except:
    #         continue
    # matchspec = re.search('specialties\D\:\s+\[\]', str(lines))
    # print(matchspec)
    # if matchspec != None:
    #     missingspec.append(matchspec)
