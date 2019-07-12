import json
import re
appenddata = []
appendindi = []
with open('C:\myfiles\QA\projectfiles\\vericred_project\\vericred_providersearch_vnsnychoice_org_20190709.json\\vericred_providersearch_vnsnychoice_org_20190709.json', buffering=900000) as f:
    for i in f:
        data = json.loads(i)
        ptype = data['provider']['provider_type']
        if ptype == 'facility':
            jsondata = re.sub('\"office_name\D+\s+\D.*phones','"office_name": "", "phones', i)
            appenddata.append(jsondata)

        if ptype == 'individual':
            appendindi.append(i)
finaldata = appendindi+appenddata


with open('C:\myfiles\QA\projectfiles\\vericred_project\\vericred_providersearch_vnsnychoice_org_20190709.json\\vericred_providersearch_vnsnychoice_org_20190709_office_removed.json', 'w', buffering=900000) as jsonfile:
    for lines in finaldata:
        jsonfile.write(lines)
