import pandas as pd
import re

uniqueplacement = []
keywordallunique = []
key = []
keywordval = []
splitkey = []
splitkey1 = []

df = pd.read_csv('C:\myfiles\QA\grepserpython\generalscripts_python\\flywheel\\201906271204-Amazon-com-SOV-Base-2019-06-27.csv', encoding='latin')

df1 = df['Placement']
df2 = df['Keyword']

for val_plac in df1:
    uniqueplacement.append(val_plac)

unique_plac_grp = df1.groupby(uniqueplacement).size().reset_index(name='count').sort_values(['count'], ascending=False)
placindex = unique_plac_grp['index']
placindex_len = len(placindex)


for valplacement, valkeyword in zip(df1, df2):
    keywordallunique.append(valkeyword)

    for plac_val in range(1, placindex_len):
        if valplacement in placindex[plac_val]:
            key.append((valplacement, valkeyword))
abc = set(key)
for valls in abc:
    splitkey.append(valls)
dfnew = pd.DataFrame(splitkey)
keyw = dfnew[0]
plac = dfnew[1]
unique_placement = dfnew.groupby(keyw).size().reset_index(name='count').sort_values(['count'], ascending=False)
# unique_keyword = dfnew.groupby(plac).size().reset_index(name='count').sort_values(['count'], ascending=False)
print(unique_placement)

