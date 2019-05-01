import psycopg2 as ps
import json
import pandas as pd
import re
from tabulate import tabulate

pd.set_option('display.max_rows', 1200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1500)
pd.set_option('max_colwidth', 50)
pd.options.display.max_colwidth = 20000

conn = ps.connect(database="vericred", user="postgres", password="mukesh", host="127.0.0.1", port="5432")
cur = conn.cursor()

addappend = []
missingadd = []
zipappend = []
missingzip = []
stateappend = []
statemissing = []
languageappend = []
languagemissing = []
officename = []
appendoffice = []
netappend = []
nettier = []
missingnet = []
tiermissing = []
phnappend = []
missingph = []
cityappend = []
citymissing = []
specappend = []
missingspec = []

cur.execute("select tablename from pg_tables where schemaname = 'public'")
tbname = cur.fetchall()
print('===================================')
print('Table Names:')
print('===================================')
for tnames in tbname:
    retname = re.sub("^\('|\'\,\)$", '', str(tnames))
    print(retname)
print('\n')
tablename1 = input('Enter tablename: ')
cur.execute("SELECT data from public.{}".format(tablename1))
rows = cur.fetchall()
for lines in rows:
    data = json.dumps(lines, sort_keys=False)
    readjson = json.loads(data)
    for add in readjson:
        try:
            addressstring = add['addresses'][0]['address_string']
            addappend.append(addressstring)
        except:
            continue
        try:
            zip = add['addresses'][0]['zip']
            zipappend.append(zip)
        except:
            continue
        try:
            state = add['addresses'][0]['state']
            stateappend.append(state)
        except:
            continue
        try:
            office = add['addresses'][0]['office_name']
            officename.append(office)
        except:
            continue
        try:
            language = add['addresses'][0]['languages']
            for lang in language:
                languagefinal = (lang['name'])
                languageappend.append(languagefinal)
        except:
            continue
        try:
            city = add['addresses'][0]['city']
            cityappend.append(city)
        except:
            continue

        match = re.search('languages\D+\s\[\]', str(readjson))
        if match != None:
            languagemissing.append(match)

        try:
            phonenum = add['addresses'][0]['phones']
            for phone in phonenum:
                phonevalue = (phone['value'])
                phnappend.append(phonevalue)
        except:
            continue
        match = re.search('phones\D+\s\[\]', str(readjson))
        if match != None:
            missingph.append(match)

        try:
            network = add['networks'][0]['name']
            netappend.append(network)
            networktier = add['networks'][0]['tier']
            nettier.append(networktier)
        except:
            continue

        matchtier = re.search('\"tier\D+null\}', str(readjson))
        if matchtier == None:
            tiermissing.append(matchtier)

        try:
            speciality = add['specialties'][0]['name']
            specappend.append(speciality)

        except:
            continue
    matchspec = re.search('specialties\D\:\s+\[\]', str(lines))
    if matchspec != None:
        missingspec.append(matchspec)

    matchnet = re.search('networks\D+\s\[\]', str(readjson))
    if matchnet != None:
        missingnet.append(matchnet)

for zips in zipappend:
    if zips == '':
        missingzip.append(zips)

for states in stateappend:
    if states == '':
        statemissing.append(states)

for offices in officename:
    if offices == '':
        appendoffice.append(offices)

for address in addappend:
    if address == '':
        missingadd.append(address)

for cities in cityappend:
    if cities == '':
        citymissing.append(cities)

dfadd = pd.DataFrame(addappend, columns=['summary Address'])
dfzip = pd.DataFrame(zipappend, columns=['summary Zip'])
dfstate = pd.DataFrame(stateappend, columns=['Summary State'])
dflan = pd.DataFrame(languageappend, columns=['summary Language'])
dfofc = pd.DataFrame(officename, columns=['summary Office'])
dfphn = pd.DataFrame(phnappend, columns=['summary Phone'])
dfcity = pd.DataFrame(cityappend, columns=['summary City'])
dfnet = pd.DataFrame(netappend, columns=['summary Network'])
dftier = pd.DataFrame(nettier, columns=['summary Tier'])
dfspec = pd.DataFrame(specappend, columns=['summary Tier'])

print('\n')
print('===================================')
print('Report Summary for', tablename1)
print('===================================')
print('Total Data Count:', len(rows))
print("===================================")
print('\n')

print('========================= ADDRESSES =========================')
print('\n')
print('=============== ADDRESS STRING ===============')
peradd = len(missingadd)/len(addappend)*100
totaladd = len(addappend)
missingaddcount = len(missingadd)
roundadd = round(peradd, 3)
print(tabulate([['Total', totaladd], ['Missing', missingaddcount, str(roundadd)+'(%)']],
               [], 'fancy_grid'))
print(dfadd.describe())
print("==========================================")
print('\n')

print('=============== ZIPCODE ===============')
perzip = len(missingzip)/len(zipappend)*100
zipper = len(zipappend)
zipcount = len(missingzip)
roundzip = round(perzip, 3)
print(tabulate([['Total', zipper], ['Missing', zipcount, str(roundzip)+'(%)']],
               [], 'fancy_grid'))
print(dfzip.describe())
print("==========================================")
print('\n')

print('=============== CITY ===============')
cityval = len(citymissing)/len(cityappend)*100
cityto = len(cityappend)
citypercent = len(citymissing)
roundcity = round(cityval, 3)
print(tabulate([['Total', cityto], ['Missing', citypercent, str(roundcity)+'(%)']],
               [], 'fancy_grid'))
print(dfcity.describe())
print("==========================================")
print('\n')

print('=============== STATE ===============')
stateval = len(statemissing)/len(stateappend)*100
stateto = len(stateappend)
stateper = len(statemissing)
roundstate = round(stateval, 3)
print(tabulate([['Total', stateto], ['Missing', stateper, str(roundstate)+'(%)']],
               [], 'fancy_grid'))
print(dfstate.describe())
print("==========================================")
print('\n')

print('=============== LANGUAGE ===============')
perlan = len(languagemissing)/len(rows)*100
langu = len(rows)
percentcount = len(languagemissing)
roundper = round(perlan, 3)
print(tabulate([['Total', langu], ['Missing', percentcount, str(roundper)+'(%)']],
               [], 'fancy_grid'))
print(dflan.describe())
print("==========================================")
print('\n')

print('=============== OFFICE NAME ===============')
perofc = len(appendoffice)/len(officename)*100
ofc = len(officename)
ofcpercent = len(appendoffice)
roundofc = round(perofc, 3)
print(tabulate([['Total', ofc], ['Missing', ofcpercent, str(roundofc)+'(%)']],
               [], 'fancy_grid'))
print(dfofc.describe())
print("==========================================")
print('\n')

print('=============== PHONE VALUE ===============')
perphn = len(missingph)/len(phnappend)*100
phn = len(phnappend)
phnpercent = len(missingph)
roundphn = round(perphn, 3)
print(tabulate([['Total', phn], ['Missing', phnpercent, str(roundphn)+'(%)']],
               [], 'fancy_grid'))
print(dfphn.describe())
print("==========================================")
print('\n')

print('========================= NETWORK =========================')

print('\n')
pernet = len(missingnet)/len(netappend)*100
netlen = len(netappend)
netpercent = len(missingnet)
roundnet = round(pernet, 3)
tiernet = len(tiermissing)/len(nettier)*100
totaltier = len(nettier)
tierlen = len(tiermissing)
roundtier = round(tiernet, 3)
print(tabulate([['Total Network', netlen], ['Missing Network', netpercent, str(roundnet)+'(%)'], ['Total Tier', totaltier], ['Missing Tier', tierlen, str(roundtier)+'(%)']],
               [], 'fancy_grid'))
print(dfnet.describe())
print("==========================================")
print(dftier.describe())
print("==========================================")
print('\n')
# cur.execute("select distinct(jsonb_array_elements_text(data->'networks')), "
#             "count(data->'networks') from public.{} group by (data->'networks') order by 1 desc".format(tablename1))
# net = cur.fetchall()
# print('=============== GROUP BY COUNT NETWORK ===============\n')
# for network in net:
#     reg = re.sub('^\D+name\'\D\s+|\}\]|\)|\'|\(\{\D+name\":\s+\D|\(|\"|\{|\}', '', str(network))
#     sp = reg.split(',')
#     networname = 'network {}'.format(sp[0]), sp[1], 'count:{}'.format(sp[2])
#     print(tabulate([networname], tablefmt="fancy_grid"))
#
# print('\n')


# print('========================= specialties =========================')
# cur.execute("select distinct(jsonb_array_elements_text(data->'specialties')), "
#             "count((data->'specialties')) from public.{} group by (data->'specialties') order by 1".format(tablename1))
# spec = cur.fetchall()
# print('=============== GROUP BY COUNT SPECIALITIES ===============\n')
# for speciality in spec:
#     regspec = re.sub('^\D+name\'\D\s+|\}\]|\)|\'|\(\{\D+name\":\s+\D|\(|\"|\{|\}|name\":\s+', '', str(speciality))
#     specappend.append(regspec)

acceptingnewpatient = []
acptrue = []
facilityname = []
fname = []
mname = []
lname = []
uname = []
gen = []
genmale = []
genfemale = []
lnum = []
npinum = []
pcpnum = []
pcptrue = []
pcpid = []
ptype = []
ptypeind = []
ptypefac = []
suid = []

print('========================= PROVIDER =========================\n')
cur.execute("select data->'provider' from public.{}".format(tablename1))
providers = cur.fetchall()
totalprovider = len(providers)
for pro in providers:
    accepting_new_patients = pro[0]['accepting_new_patients']
    facility_name = pro[0]['facility_name']
    first_name = pro[0]['first_name']
    middle_name = pro[0]['middle_name']
    last_name = pro[0]['last_name']
    unparsed_name = pro[0]['unparsed_name']
    gender = pro[0]['gender']
    license_number = pro[0]['license_number']
    npi = pro[0]['npi']
    pcp = pro[0]['pcp']
    pcp_id = pro[0]['pcp_id']
    provider_type = pro[0]['provider_type']
    site_uid = pro[0]['site_uid']
    # suffix = pro[0]['suffix']
    # title = pro[0]['title']
    # ftype = pro[0]['facility_type']
    if accepting_new_patients == None:
        acceptingnewpatient.append(accepting_new_patients)
    if accepting_new_patients == True:
        acptrue.append(accepting_new_patients)
    if facility_name == None:
        facilityname.append(facility_name)
    if first_name == None:
        fname.append(first_name)
    if middle_name == None:
        mname.append(middle_name)
    if last_name == None:
        lname.append(last_name)
    if unparsed_name == None:
        uname.append(unparsed_name)
    if gender == None:
        gen.append(gender)
    if gender == 'Male' or gender == 'M':
        genmale.append(gender)
    if gender == 'Female' or gender == 'F':
        genfemale.append(gender)
    if license_number == None:
        lnum.append(license_number)
    if npi == None:
        npinum.append(npi)
    if pcp == None:
        pcpnum.append(pcp)
    if pcp == True:
        pcptrue.append(pcp)
    if pcp_id == None:
        pcpid.append(pcp_id)
    if provider_type == None:
        ptype.append(provider_type)
    if provider_type == 'individual':
        ptypeind.append(provider_type)
    if provider_type == 'facility':
        ptypefac.append(provider_type)
    if site_uid == None:
        suid.append(site_uid)

peracceptnew = round(len(acceptingnewpatient)/totalprovider*100, 3)
pertrue = round(len(acptrue)/totalprovider*100, 3)
facilityper = round(len(facilityname)/totalprovider*100, 3)
fnameper = round(len(fname)/totalprovider*100, 3)
mnameper = round(len(mname)/totalprovider*100, 3)
lnameper = round(len(lname)/totalprovider*100, 3)
unameper = round(len(uname)/totalprovider*100, 3)
missinggender = round(len(gen)/totalprovider*100, 3)
missingmale = round(len(genmale)/totalprovider*100, 3)
missingfemale = round(len(genfemale)/totalprovider*100, 3)
licnum = round(len(lnum)/totalprovider*100, 3)
npinumber = round(len(npinum)/totalprovider*100, 3)
pcpto = round(len(pcpnum)/totalprovider*100, 3)
pcptrueto = round(len(pcptrue)/totalprovider*100, 3)
pcpidnum = round(len(pcpid)/totalprovider*100, 3)
ptypeto = round(len(ptype)/totalprovider*100, 3)
ptypeindper = round(len(ptypeind)/totalprovider*100, 3)
ptypefacper = round(len(ptypefac)/totalprovider*100, 3)
siteuid = round(len(suid)/totalprovider*100, 3)

print(tabulate([['Total Provider', totalprovider, 'Percentage (%)'], ['Missing Accepting New Patient', len(acceptingnewpatient), peracceptnew],
                ['Accepting New Patient (True)', len(acptrue), pertrue], ['Missing Facility Name', len(facilityname), facilityper],
                ['Missing First Name', len(fname), fnameper], ['Missing Second Name', len(mname), mnameper]
                , ['Missing Last Name', len(lname), lnameper], ['Missing Unparsed Name', len(uname), unameper],
                ['Missing Gender', len(gen), missinggender], ['Missing Male', len(genmale), missingmale],
                ['Missing Female', len(genfemale), missingfemale], ['Missing License', len(lnum), licnum],
                ['Missing NPI', len(npinum), npinumber], ['Missing PCP', len(pcpnum), pcpto],
                ['PCP (True)', len(pcptrue), pcptrueto], ['Missing PCP_ID', len(pcpid), pcpidnum],
                ['Missing Provider', len(ptype), ptypeto], ['Provider (individual)', len(ptypeind), ptypeindper],
                ['Provider (facility)', len(ptypefac), ptypefacper], ['Missing Site_Uid', len(suid), siteuid]], tablefmt='fancy_grid'))


print("==========================================")
print('\n')
print('========================= SPECIALITIES =========================')
spec = len(missingspec)/len(specappend)*100
specto = len(specappend)
specmis = len(missingspec)
roundspec = round(spec, 3)
print(tabulate([['Total', specto], ['Missing', specmis, str(roundspec)+'(%)']],
               [], 'fancy_grid'))
print(dfspec.describe())
print("==========================================")
print('\n')


conn.commit()
