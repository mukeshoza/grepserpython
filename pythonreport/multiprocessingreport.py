import psycopg2 as ps
import json
import pandas as pd
import re
from tabulate import tabulate
import multiprocessing as mp

pd.set_option('display.max_rows', 1200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1500)
pd.set_option('max_colwidth', 50)
pd.options.display.max_colwidth = 20000

conn = ps.connect(database="vericred", user="postgres", password="mukesh", host="127.0.0.1", port="5432")
cur = conn.cursor()


def spawn():
    cur.execute("select (data) from humanadentalnew")
    rows = cur.fetchall()
    for lines in rows:
        print(lines)

if __name__ == '__main__':
    p = mp.Process(target=spawn)
    p.start()
