import pickle
import json

dataappend = []
with open('C:\myfiles\QA\projectfiles\\vericred_project\\vericred_prismisp_mvp_20190410.json\\vericred_prismisp_mvp_20190410.json', 'rb') as f:
    for lines in f:
        data = json.loads(lines)
        try:
            dataappend.append(data)
        except:
            continue
        # print(data)
pickle_out = open("nationwide.pickle", "wb")
pickle.dump(dataappend, pickle_out)
pickle_out.close()

pickle_in = open("nationwide.pickle", "rb")
example_dict = pickle.load(pickle_in)
for line in example_dict:
    print(line['addresses'][0]['state'])
