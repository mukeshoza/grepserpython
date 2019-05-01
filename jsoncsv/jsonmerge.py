import pandas as pd
from jsonmerge import merger

df = pd.read_json('vericerd.json', lines=True)
df1 = pd.read_json('vericred_upmc_20181121.json', lines=True)

base = merger.merge(base, v1, meta={'version': 1})
