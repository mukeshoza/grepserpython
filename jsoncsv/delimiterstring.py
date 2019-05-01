import csv
import pandas as pd

with open('datas.csv', 'r') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
     for row in reader:
         for i, cell in enumerate(row):
            print((cell))
