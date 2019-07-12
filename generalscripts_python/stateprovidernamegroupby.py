import json
import pandas as pd

stateappend = []
provi = []
with open('C:\myfiles\QA\projectfiles\\vericred_project\\vericred_anthem\\vericred_anthem.json', buffering=90000000) as f:
    for i in f:
        data = json.loads(i)
        add = data['addresses']
        for states in add:
            st = states['state']
            stateappend.append(st)
        prov = data['provider']['unparsed_name']
        finaldata = st, prov
        provi.append(finaldata)

df = pd.DataFrame(provi)
print(df)

