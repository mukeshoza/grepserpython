appendjson = []
with open('testdental.json', buffering=90000000) as f:
    for lines in f:
        appendjson.append(lines)

abc = set(appendjson)
duplicatecount = len(appendjson)-len(abc)
if duplicatecount >= 1:
    print('Duplicate lines found')
    print('Total Duplicates = ', duplicatecount)
else:
    print('No duplicate lines found')
with open('new.json', 'w', buffering=90000000) as new:
    for line in abc:
        new.write(line)