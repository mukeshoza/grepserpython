import json

appendata = []
with open('C:\myfiles\QA\projectfiles\\vericred_project\\vericred_wellmark_20190423.json\\merged_wellmark.json', buffering=900000000) as f:
    for lines in f:
        data = json.loads(lines)
        pro = data['provider']['unparsed_name']
        appendata.append(pro)
for unname in appendata:
    print(unname)