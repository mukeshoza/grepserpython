import json
import pandas as pd
import re

ofcappend = []
hosappend = []
with open('reportjsonsample.json', 'r') as f:
    for lines in f:
        datastr = str(lines)
        rep = re.sub('\'\'|none|None|NONE', 'null', datastr)
        data = json.loads(rep)
        for add in data['addresses']:
            offc = add['office_name']
            ofcappend.append(offc)
        for hos in data['hospital_affiliations']:
            hosp = hos['name']
            hosappend.append(hosp)
    lendata = len(hosappend)


    df = pd.DataFrame(ofcappend)
    # print(len(df[0])-df.count())
    missing = df.isna()
    ma = missing.sum()
    meanstate = missing.mean().round(3)*100
    print(meanstate)




