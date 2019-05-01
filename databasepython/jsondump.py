import json
import re


jsonline = input('Json Line to Dump: ')
jsonread = json.loads(jsonline)

# rep = re.sub('\\n|\\r|\\t', '', lines)
dumpjson = json.dumps(jsonread, indent=4, sort_keys=False)
print('Dumped JSOON value is:\n', dumpjson)





