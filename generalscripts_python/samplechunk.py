import pandas as pd
import json

appendl = []
chunksize = 30000
df = pd.read_json('deduped.json', chunksize=chunksize, lines=True)
for lines in df:
    appendl.append(lines)
