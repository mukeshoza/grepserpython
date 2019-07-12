import pandas as pd
import hashlib
import random
import string

d0 = pd.read_csv('./E0.csv')
d1 = d0[['Date','HomeTeam','FTR','HTR','Referee']].dropna()
print(d1.head())
# Get a unique list of the clear text, as a List
tmplist = list(set(d1['HomeTeam']))
# Add some random characters before and after the team name.
# Structured them in a Dictionary
# Example -- Liverpool -> aaaaaaaLiverpoolbbbbbbbb
mapping1 = {i : (''.join(random.choice(string.hexdigits) for i in range(12)))+i+(''.join(random.choice(string.hexdigits) for i in range(12)))  for i in tmplist}
# Create a DF to leave the original DF intact.
d2 = d1.copy()
# Create a new column containing clear_text_Nonce
d2['newname'] = [mapping1[i] for i in d2['HomeTeam']]
print(d2.head())
# Hash the clear_text+Nonce string
d2['hash'] = [hashlib.sha1(str.encode(str(i))).hexdigest() for i in d2['newname']]
print(d2.head())
# To proof that the same clear text has the same Hash string.
print(d2[d2['HomeTeam']=='Chelsea'].tail(30))
# Create a new DF with the clear-text column removed.
d3 = d2[['Date','hash','FTR','Referee']].rename(columns={'hash':'HomeTeamHash'})
print(d3.head())