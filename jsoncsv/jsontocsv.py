import pandas as pd
import json


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 50)


jsonfile = pd.read_json('samplevericred.json', lines=True)
fun = jsonfile
# print(fun.head())

# fun.to_json('samplevericred.json', orient='records', lines=True)

for address in fun['addresses'][700]:
    addressstring = (address['address_string'], address['city'])
    print(addressstring)

    for langu in address['languages']:
        lang1 = langu['name'], langu['type']
        print(lang1)

    for phn in address['phones']:
        phnno = phn['type'], phn['value']
        print(phnno)


    # a = json.dumps(addressstring)
    # b = json.dumps(com)
    # print(a+b)
