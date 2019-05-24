import copy
import json
#
# append1 = []
# append2 = []
# with open('sample1.json', buffering=90000000) as f:
#     for lines in f:
#         data = json.loads(lines)
#         append1.append(data)
#
# with open('sample2.json', buffering=90000000) as f1:
#     for line in f1:
#         datas = json.loads(line)
#         append2.append(datas)
# appendfinal = []
# append1 = copy.copy(append1 + append2)
# for liness in append1:
#    appendfinal.append(liness)
#
# with open('files.json','w', buffering=90000000) as w:
#     for da in appendfinal:
#         json.dump(da, w)
#         w.write('\n')
appendalls = []
uidsappend = []
filenames = ['sample1.json', 'sample2.json']
with open('files.json', 'w', buffering=90000000) as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
                appendalls.append(line)

for lines in appendalls:
    data = json.loads(lines)
    dic = dict(data)
    siteuid = dic['provider']['site_uid']