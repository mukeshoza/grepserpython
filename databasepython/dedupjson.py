import json
import jsondiff

app = []
with open('/Users/mukesh/Documents/myprojects/projectfiles/vericredprojects/UHC/UHC_Nation.json','r') as f:
    for lines in f:
        ab =json.loads(lines)
        # app.append(lines)

appe = []
with open('sample.json','r') as a:
    for line in a:
        bc = json.loads(line)
        # appe.append(line)

    diffe = jsondiff.diff(ab, bc)
    print(diffe)





