import json
from tabulate import tabulate
# import pandas as pd

appenddata = []
addressblank = []

with open('deduped.json', buffering=90000000) as sumdata:
    size = sum(1 for _ in sumdata)

with open('deduped.json', buffering=90000000) as f:
    for i in f:
        data = json.loads(i)
        # print(data)
        # appenddata.append(data)
        for lines in data['addresses']:
            a = lines['address_string']
            appenddata.append(a)
            if a == '' or None:
                addressblank.append(a)

# df = pd.DataFrame(appenddata)
# grophead = df.groupby(appenddata).size().head().sort_values(ascending=False)
# print(df.describe())
totalprovider = size
addblank = len(addressblank)
totaladd = totalprovider-addblank
per = (addblank/totalprovider*100)


add1 = '<style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 80%;}' \
      '\ntd, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}' \
      '\ntr:nth-child(even) {background-color: #dddddd;}\n</style><h2>Vericred Summary Report</h2>\n' +\
      tabulate([['Total Provider', totalprovider], ['<b>Addresses</b>'],
                ['Missing address_string', addblank], ['Total address_string', totaladd]],tablefmt='html')



with open('sample.html', 'w', buffering=90000000) as html:
    html.write(add1)