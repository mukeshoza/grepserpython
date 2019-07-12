import json
import re
import pandas as pd

addressblank = []
cityappend = []
languageappend = []
officeappend = []
phoneappend = []
stateappend = []
zipappend = []
accnewpatappend = []
fnameappend = []
ftypeappend = []
firstname = []
mname = []
lname = []
uname = []
gender = []
npi = []
pcp = []
pcpid = []
ptypeind = []
ptypefac = []
suid = []
networks = []
netgrp = []
tier = []
groupaff = []
hospaff = []
spec = []
netgrpby = []
countnet = []
stategrby = []
statecount = []
statappend = []
netlist = []
appendnet = []
indexnet = []
netcount = []
netval = []
indexstate = []
countstate = []

filename = 'C:\myfiles\QA\projectfiles\\vericred_project\\vericred_usable_20190626.json\\vericred_usable_20190626.json'
namefile = re.sub("\w+:\D\w+.*\\\\|.json$",'', filename)
with open(filename, buffering=90000000) as sumdata:
    size = sum(1 for _ in sumdata)

with open(filename, buffering=90000000) as f:
    for i in f:
        data = json.loads(i)
        dicti = dict(data)
        for lines in data['addresses']:
            addstng = lines['address_string']
            if addstng == '' or None:
                addressblank.append(addstng)

            city = lines['city']
            if city == '' or None:
                cityappend.append(city)

            try:
                match = re.search('languages\D+\s\[\]', str(data))
                if match != None:
                 languageappend.append(match)
            except:
                continue
            # for names in language:
            #     lang = names['name']
            officename = lines['office_name']
            if officename == '' or None:
                officeappend.append(officename)

            phoneval = re.search('phones\D+\s\[\]', str(data))
            if phoneval != None:
                phoneappend.append(phoneval)

            state = lines['state']
            statappend.append(state)
            if state == '' or None:
                stateappend.append(state)

            zip1 = lines['zip']
            if zip1 == '' or None:
                zipappend.append(zip1)

        anp = dicti['provider']['accepting_new_patients']
        if anp == None or '':
            accnewpatappend.append(anp)

        npiname = dicti['provider']['npi']
        if npiname == '' or None:
            npi.append(npiname)

        pcpname = dicti['provider']['pcp']
        if pcpname == None or '':
            pcp.append(pcpname)

        pcpidname = dicti['provider']['pcp_id']
        if pcpidname == None or '':
            pcpid.append(pcpidname)

        site_uid = dicti['provider']['site_uid']
        if site_uid == '' or None:
            suid.append(site_uid)

        unpname = dicti['provider']['unparsed_name']
        if unpname == '' or None:
            uname.append(unpname)

        try:
            protype = dicti['provider']['provider_type']
            if protype == 'facility':
                ptypefac.append(protype)

                facname = dicti['provider']['facility_name']
                if facname == '' or None:
                    fnameappend.append(facname)

                ftype = dicti['provider']['facility_type']
                if ftype == '' or None:
                    ftypeappend.append(ftype)

            if protype == 'individual':
                ptypeind.append(protype)

                finame = dicti['provider']['first_name']
                if finame == '' or None:
                    firstname.append(finame)

                laname = dicti['provider']['last_name']
                if laname == '' or None:
                    lname.append(laname)

                miname = dicti['provider']['middle_name']
                if miname == '' or None:
                    mname.append(miname)

                gen = dicti['provider']['gender']
                gen1 = re.search('gender\': None', str(data))
                if gen == '' or None or gen1 != None:
                    gender.append(gen)
        except:
            continue

        try:
            network = re.search('networks\D+\s\[\]', str(data))
            if network != None:
                networks.append(network)
        except:
            continue
        for net in data['networks']:
            tiername = net['tier']
            networkgroup = net['name']
            netgrp.append(networkgroup)
            if tiername == None or '':
                tier.append(tiername)
        try:
            grpaff = re.search('group_affiliations\"\:\s+\[\]', i)
            if grpaff != None:
                groupaff.append(groupaff)

            hosaff = re.search('hospital_affiliations\"\:\s+\[\]', i)
            if hosaff != None:
                hospaff.append(hospaff)

            specialities = re.search('specialties\"\:\s+\[\]', i)
            if specialities != None:
                spec.append(specialities)
        except:
            continue



df = pd.DataFrame(netgrp, columns=['networkname'])
grpnet = df.groupby(netgrp).size().reset_index(name='count').sort_values(['count'], ascending=False)
headnet = grpnet.head(10)
othernet = grpnet[10:]['count'].sum()

for values in headnet['index']:
    netgrpby.append(values)

for values1 in headnet['count']:
    countnet.append(values1)

netgrpby.append('Others')
countnet.append(othernet)

nettable = '''<a style = "margin-left:6%;" class="btn btn-dark" data-toggle="collapse" href="#multiCollapseExample1" role="button" aria-expanded="false" aria-controls="multiCollapseExample1">All Networks</a>
  <button  style = "margin-right:-30%; float:right;" class="btn btn-dark" type="button" data-toggle="collapse" data-target="#multiCollapseExample2" aria-expanded="false" aria-controls="multiCollapseExample2">All States</button>
  
<div class="row">
  <div class="col">
    <div class="collapse multi-collapse" id="multiCollapseExample1">
      <table class="table table-hover">
  <table class="table table-hover" style="width:40%; margin-left: 6%;">
  <thead>
    <tr>'''
tabnet1 = '<th scope="col" style="width:40%";>{}</th>'.format('Networks')
tabnet2 = '<th scope="col" style="width:40%";>{}</th>'.format('Count')

tabnet3 = '''</tr></thead><tbody>'''

val1 = grpnet['index']
val2 = grpnet['count']

for (val, vals) in zip(val1, val2):
    a = '<tr><td scope="row">{}</td>'.format(val)
    b = '<td>{}</td></tr>'.format(vals)
    ab = indexnet.append(a)
    indexnet.append(b)

subnet = re.sub("\[|\]|\'|\,", '', str(indexnet))
finalsub = subnet

tabnet4 = '''
  </tbody>
</table></div></div></div>'''

nettableall = nettable+tabnet1+tabnet2+tabnet3+finalsub+tabnet4


df1 = pd.DataFrame(statappend, columns=['state'])
statcount = df1.groupby(statappend).size().reset_index(name='count').sort_values(['count'], ascending=False)
statehead = statcount.head(10)
otherstate = statcount[10:]['count'].sum()

for valuestate in statehead['index']:
    stategrby.append(valuestate)
for valuesstate1 in statehead['count']:
    statecount.append(valuesstate1)

stategrby.append('Others')
statecount.append(otherstate)

statetable = '''<div class="col">
    <div class="collapse multi-collapse" id="multiCollapseExample2">
      <table class="table table-hover">
    
    <table class="table table-hover" style="width:25%; margin-left: 75%;">
  <thead>
    <tr>'''
tabstate1 = '<th scope="col" style="width:40%";>{}</th>'.format('States')
tabstate2 = '<th scope="col" style="width:40%";>{}</th>'.format('Count')

tabstate3 = '''</tr></thead><tbody>'''

valstate1 = statcount['index']
valstate2 = statcount['count']

for (valst, valst1) in zip(valstate1, valstate2):
    astate = '<tr><td scope="row">{}</td>'.format(valst)
    bstate = '<td>{}</td></tr>'.format(valst1)
    abstate = indexstate.append(astate)
    indexstate.append(bstate)

substate = re.sub("\[|\]|\'|\,", '', str(indexstate))
finalstate = substate

tabstate4 = '''
  </tbody>
</table></div></div></div>'''

statetableall = statetable+tabstate1+tabstate2+tabstate3+finalstate+tabstate4

totalprovider = size
addblank = len(addressblank)
totaladd = totalprovider - addblank
per = (addblank / totalprovider * 100)

cityblank = len(cityappend)
totalcity = totalprovider - cityblank
percity = (cityblank / totalprovider * 100)

languageblank = len(languageappend)
totallang = totalprovider - languageblank
perlang = (languageblank / totalprovider * 100)

officeblank = len(officeappend)
totaloffice = totalprovider - officeblank
peroffice = (officeblank / totalprovider * 100)

phoneblank = len(phoneappend)
phonetotal = totalprovider - phoneblank
perphone = (phoneblank / totalprovider * 100)

stateblank = len(stateappend)
statetotal = totalprovider - stateblank
perstate = (stateblank / totalprovider * 100)

zipblank = len(zipappend)
ziptotal = totalprovider - zipblank
perzip = (zipblank / totalprovider * 100)

anpblank = len(accnewpatappend)
anptotal = totalprovider - anpblank
peranp = (anpblank / totalprovider * 100)

npiblank = len(npi)
npitotal = totalprovider - npiblank
pernpi = (npiblank / totalprovider * 100)

pcpblank = len(pcp)
pcptotal = totalprovider - pcpblank
perpcp = (pcpblank / totalprovider * 100)

suidblank = len(suid)
suidtotal = totalprovider - suidblank
persuid = (suidblank / totalprovider * 100)

unameblank = len(uname)
unametotal = totalprovider - unameblank
peruname = (unameblank / totalprovider * 100)

pindi = len(ptypeind)
perindi = (pindi / totalprovider * 100)

pfaci = len(ptypefac)
perfaci = (pfaci / totalprovider * 100)

if pfaci > 1:
    facnameblank = len(fnameappend)
    totalfname = pfaci - facnameblank
    perfacname = (facnameblank / pfaci * 100)

    ftypeblank = len(ftypeappend)
    totalftype = pfaci - ftypeblank
    perftype = (ftypeblank / pfaci * 100)
else:
    pass

fnameblank = len(firstname)
totalfirstname = pindi - fnameblank
perfname = (fnameblank / pindi * 100)

lnameblank = len(lname)
totallname = pindi - lnameblank
perlname = (lnameblank / pindi * 100)

mnameblank = len(mname)
totalmname = pindi - mnameblank
permname = (mnameblank / pindi * 100)

genderblank = len(gender)
totalgender = pindi - genderblank
pergender = (genderblank / pindi * 100)

networkblank = len(networks)
totalnetworks = totalprovider - networkblank
pernet = (networkblank / totalprovider * 100)

tierblank = len(tier)
totaltier = totalprovider-tierblank
pertier = (tierblank / totalprovider * 100)

grpblank = len(groupaff)
totalgrp = totalprovider - grpblank
pergrp = (grpblank / totalprovider * 100)

hosblank = len(hospaff)
totalhosp = totalprovider - hosblank
perhosp = (hosblank / totalprovider * 100)

specblank = len(spec)
totalspec = totalprovider - specblank
perspec = (specblank / totalprovider * 100)

if per > 8:
    result = '<b><font color = "red">address_string</b></font>'
else:
    result = '<b><font color = "green">address_string</b></font>'

if percity > 8:
    resultcity = '<b><font color = "red">city</b></font>'
else:
    resultcity = '<b><font color = "green">city</b></font>'

if perlang > 15:
    resutllang = '<b><font color = "red">language</b></font>'
else:
    resutllang = '<b><font color = "green">language</b></font>'

if peroffice > 15:
    resultofc = '<b><font color = "red">office_name</b></font>'
else:
    resultofc = '<b><font color = "green">office_name</b></font>'

if perphone > 15:
    resultphone = '<b><font color = "red">phone</b></font>'
else:
    resultphone = '<b><font color = "green">phone</b></font>'

if perstate > 8:
    resultstate = '<b><font color = "red">state</b></font>'
else:
    resultstate = '<b><font color = "green">state</b></font>'

if perzip > 8:
    resultzip = '<b><font color = "red">zip</b></font>'
else:
    resultzip = '<b><font color = "green">zip</b></font>'

if peranp > 18:
    resultanp = '<b><font color = "red">accepting_new_patient</b></font>'
else:
    resultanp = '<b><font color = "green">accepting_new_patient</b></font>'

if pernpi > 18:
    resultnpi = '<b><font color = "red">npi</b></font>'
else:
    resultnpi = '<b><font color = "green">npi</b></font>'

if perpcp > 18:
    resultpcp = '<b><font color = "red">pcp</b></font>'
else:
    resultpcp = '<b><font color = "green">pcp</b></font>'

if persuid > 8:
    resultsuid = '<b><font color = "red">site_uid</b></font>'
else:
    resultsuid = '<b><font color = "green">site_uid</b></font>'

if peruname > 5:
    resultuname = '<b><font color = "red">Unparsed Name</b></font>'
else:
    resultuname = '<b><font color = "green">Unparsed Name</b></font>'
if pfaci > 1:
    if perfacname > 8:
        resultfacname = '<b><font color = "red">Facility Name</b></font>'
    else:
        resultfacname = '<b><font color = "green">Facility Name</b></font>'

    if perftype > 8:
        resultftype = '<b><font color = "red">Facility Type</b></font>'
    else:
        resultftype = '<b><font color = "green">Facility Type</b></font>'
else:
    pass
if perfname > 5:
    resultfname = '<b><font color = "red">First Name</b></font>'
else:
    resultfname = '<b><font color = "green">First Name</b></font>'

if perlname > 5:
    resultlname = '<b><font color = "red">Last Name</b></font>'
else:
    resultlname = '<b><font color = "green">Last Name</b></font>'

if permname > 5:
    resultmname = '<b><font color = "red">Middle Name</b></font>'
else:
    resultmname = '<b><font color = "green">Middle Name</b></font>'

if pergender > 5:
    resultgender = '<b><font color = "red">Gender</b></font>'
else:
    resultgender = '<b><font color = "green">Gender</b></font>'

if pernet > 5:
    resultnet = '<b><font color = "red">Network</b></font>'
else:
    resultnet = '<b><font color = "green">Network</b></font>'

if pertier > 8:
    resulttier = '<b><font color = "red">Network Tier</b></font>'
else:
    resulttier = '<b><font color = "green">Network Tier</b></font>'

if pergrp > 12:
    resultgrp = '<b><font color = "red">Group Affiliations</b></font>'
else:
    resultgrp = '<b><font color = "green">Group Affiliations</b></font>'

if perhosp > 12:
    resulthosp = '<b><font color = "red">Hospital Affiliations</b></font>'
else:
    resulthosp = '<b><font color = "green">Hospital Affiliations</b></font>'

if perspec > 8:
    resultspec = '<b><font color = "red">Specialties</b></font>'
else:
    resultspec = '<b><font color = "green">Specialties</b></font>'

htmlcollapse = '''<!DOCTYPE html>
<html>
<head>
<title>Vericred Summary Report</title>
<meta charset="utf-8">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src = "https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script>

<style>
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 75%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
  margin-left: 11%;
  text-align: center
}

.active, .collapsible:hover {
  background-color: #555;
  margin-left: 11%

}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
  width: 75%;
  margin-left: 11%;
  text-align: center
}

</style>
</head>
<body>
<center>

'''
reporttitle = '<br><hr><h2>Vericred Project Summary Report - {}</h2><hr></center>'.format(namefile)
'''<div style="margin-left:10%; margin-right:10%;">
<p><b>'''

totalpro = '<b style="margin-left:6%;"><font color="purple">Total Provider: {:,}</font>'.format(totalprovider)
pertotaladd = round((totaladd/totalprovider*100), 2)
progressaddstring = '''<div class="container">
  <div class="progress">
<div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

value1 = ' aria-valuenow= "{}"'.format(pertotaladd)
value2 = ' style="width:{}%">'.format(pertotaladd)
missingprogress1 = str(pertotaladd) + '''% Total Address_String

</div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
value3 = ' aria-valuenow= "{}"'.format(per)
value4 = ' style="width:{}%">'.format(round(per, 2))
missingprogress2 = str(round(per, 2)) + '''% Missing Address_String

    </div>
  </div>
</div>'''
finaladdbar = progressaddstring + value1 + value2 + missingprogress1 + value3 + value4 + missingprogress2

addressstring = 'address_string' + finaladdbar
pertotalcity = round((totalcity/totalprovider*100), 2)

progresscity = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuecity1 = ' aria-valuenow= "{}"'.format(pertotalcity)
valuecity2 = ' style="width:{}%">'.format(pertotalcity)
missingcity1 = str(pertotalcity) + '''% Total City

    </div>
    <div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuecity3 = ' aria-valuenow= "{}"'.format(percity)
valuecity4 = ' style="width:{}%">'.format(round(percity, 2))
missingcity2 = str(round(percity, 2)) + '''% Missing City

    </div>
  </div>
</div>'''

finalcitybar = progresscity + valuecity1 + valuecity2 + missingcity1 + valuecity3 + valuecity4 + missingcity2
cities = 'city' + finalcitybar

totalper = round((totallang/totalprovider*100), 2)

progresslang = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuelang1 = ' aria-valuenow= "{}"'.format(totalper)
valuelang2 = ' style="width:{}%">'.format(totalper)
missinglang1 = str(totalper) + '''% Total Language

    </div>
    <div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuelang3 = ' aria-valuenow= "{}"'.format(perlang)
valuelang4 = ' style="width:{}%">'.format(round(perlang, 2))
missinglang2 = str(round(perlang, 2)) + '''% Missing Language

    </div>
  </div>
</div>'''

langbar = progresslang + valuelang1 + valuelang2 + missinglang1 + valuelang3 + valuelang4 + missinglang2
langu = 'Language' + langbar

perofc = round((totaloffice/totalprovider*100), 2)

progressofc = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valueofc1 = ' aria-valuenow= "{}"'.format(perofc)
valueofc2 = ' style="width:{}%">'.format(perofc)
missingofc1 = str(perofc) + '''% Total Office

    </div>
    <div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valueofc3 = ' aria-valuenow= "{}"'.format(peroffice)
valueofc4 = ' style="width:{}%">'.format(round(peroffice, 2))
missingofc2 = str(round(peroffice, 2)) + '''% Missing Office

    </div>
  </div>
</div>'''

ofcbar = progressofc + valueofc1 + valueofc2 + missingofc1 + valueofc3 + valueofc4 + missingofc2
ofc = 'Office' + ofcbar

perphn = round((phonetotal/totalprovider*100), 2)

progressphn = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuephn1 = ' aria-valuenow= "{}"'.format(perphn)
valuephn2 = ' style="width:{}%">'.format(perphn)
missingphn1 = str(perphn) + '''% Total Phone

    </div>
    <div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuephn3 = ' aria-valuenow= "{}"'.format(perphone)
valuephn4 = ' style="width:{}%">'.format(round(perphone, 2))
missingphn2 = str(round(perphone, 2)) + '''% Missing Phone

    </div>
  </div>
</div>'''

phnbar = progressphn + valuephn1 + valuephn2 + missingphn1 + valuephn3 + valuephn4 + missingphn2
phn = 'Phone<br />' + phnbar + '<br />'

perstates = round((statetotal/totalprovider*100), 2)

progressstate = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuestate1 = ' aria-valuenow= "{}"'.format(perstates)
valuestate2 = ' style="width:{}%">'.format(perstates)
missingstate1 = str(perstates) + '''% Total State

    </div>
    <div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuestate3 = ' aria-valuenow= "{}"'.format(perstate)
valuestate4 = ' style="width:{}%">'.format(round(perstate, 2))
missingstate2 = str(round(perstate, 2)) + '''% Missing State

    </div>
  </div>
</div>'''

statebar = progressstate + valuestate1 + valuestate2 + missingstate1 + valuestate3 + valuestate4 + missingstate2
stateall = 'State' + statebar

zipper = round((ziptotal/totalprovider*100), 2)

progresszip = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuezip1 = ' aria-valuenow= "{}"'.format(zipper)
valuezip2 = ' style="width:{}%">'.format(zipper)
missingzip1 = str(zipper) + '''% Total Zip

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuezip3 = ' aria-valuenow= "{}"'.format(perzip)
valuezip4 = ' style="width:{}%">'.format(round(perzip, 2))
missingzip2 = str(round(perzip, 2)) + '''% Missing Zip

    </div>
  </div></b>
</div>'''

zipbar = progresszip + valuezip1 + valuezip2 + missingzip1 + valuezip3 + valuezip4 + missingzip2
zipall = zipbar

anpper = round((anptotal/totalprovider*100), 2)
progressanp = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valueanp1 = ' aria-valuenow= "{}"'.format(anpper)
valueanp2 = ' style="width:{}%">'.format(anpper)
missinganp1 = str(round(anpper, 2)) + '''% Total Accepting New Patient

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valueanp3 = ' aria-valuenow= "{}"'.format(round(peranp, 2))
valueanp4 = ' style="width:{}%">'.format(round(peranp, 2))
missinganp2 = str(round(peranp, 2)) + '''% Missing Accepting New Patient

    </div>
  </div></b>
</div>'''

anpbar = progressanp + valueanp1 + valueanp2 + missinganp1 + valueanp3 + valueanp4 + missinganp2
anpall = 'Accepting New Patient' + anpbar

npiper = round((npitotal/totalprovider*100), 2)
progressnpi = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuenpi1 = ' aria-valuenow= "{}"'.format(npiper)
valuenpi2 = ' style="width:{}%">'.format(npiper)
missingnpi1 = str(round(npiper, 2)) + '''% Total NPI

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuenpi3 = ' aria-valuenow= "{}"'.format(round(pernpi, 2))
valuenpi4 = ' style="width:{}%">'.format(round(pernpi, 2))
missingnpi2 = str(round(pernpi, 2)) + '''% Missing NPI

    </div>
  </div></b>
</div>'''

npibar = progressnpi + valuenpi1 + valuenpi2 + missingnpi1 + valuenpi3 + valuenpi4 + missingnpi2
npiall = 'NPI' + npibar


pcpper = round((pcptotal/totalprovider*100), 2)
progresspcp = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuepcp1 = ' aria-valuenow= "{}"'.format(pcpper)
valuepcp2 = ' style="width:{}%">'.format(pcpper)
missingpcp1 = str(round(pcpper, 2)) + '''% Total PCP

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuepcp3 = ' aria-valuenow= "{}"'.format(round(perpcp, 2))
valuepcp4 = ' style="width:{}%">'.format(round(perpcp, 2))
missingpcp2 = str(round(perpcp, 2)) + '''% Missing PCP

    </div>
  </div></b>
</div>'''

pcpbar = progresspcp + valuepcp1 + valuepcp2 + missingpcp1 + valuepcp3 + valuepcp4 + missingpcp2
pcpall = 'NPI' + pcpbar


siteuisper = round((suidtotal/totalprovider*100), 2)
progresssuid = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuesite1 = ' aria-valuenow= "{}"'.format(siteuisper)
valuesite2 = ' style="width:{}%">'.format(siteuisper)
missingsite1 = str(round(siteuisper, 2)) + '''% Total site_uid

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuesite3 = ' aria-valuenow= "{}"'.format(round(persuid, 2))
valuesite4 = ' style="width:{}%">'.format(round(persuid, 2))
missingsite2 = str(round(persuid, 2)) + '''% Missing suite_uid

    </div>
  </div></b>
</div>'''

suidbar = progresssuid + valuesite1 + valuesite2 + missingsite1 + valuesite3 + valuesite4 + missingsite2
suidall = 'site_uid' + suidbar


unameper = round((unametotal/totalprovider*100), 2)
progressuname = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valueuname1 = ' aria-valuenow= "{}"'.format(unameper)
valueuname2 = ' style="width:{}%">'.format(unameper)
missinguname1 = str(round(unameper, 2)) + '''% Total unparsed_name

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valueuname3 = ' aria-valuenow= "{}"'.format(round(peruname, 2))
valueuname4 = ' style="width:{}%">'.format(round(peruname, 2))
missinguname2 = str(round(peruname, 2)) + '''% Missing unparsed_name

    </div>
  </div></b>
</div>'''

unamebar = progressuname + valueuname1 + valueuname2 + missinguname1 + valueuname3 + valueuname4 + missinguname2
unameall = 'site_uid' + unamebar

if pfaci>1:
    facper = round((totalfname/pfaci*100), 2)
    progressfacname = '''<div class="container">
      <div class="progress">
       <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

    valuefac1 = ' aria-valuenow= "{}"'.format(facper)
    valuefac2 = ' style="width:{}%">'.format(facper)
    missingfac1 = str(round(facper, 2)) + '''% Total Facility Name
    
        </div>
    <div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
    valuefac3 = ' aria-valuenow= "{}"'.format(round(perfacname, 2))
    valuefac4 = ' style="width:{}%">'.format(round(perfacname, 2))
    missingfac2 = str(round(perfacname, 2)) + '''% Missing Facility Name
    
        </div>
      </div></b>
    </div>'''

    facnamebar = progressfacname + valuefac1 + valuefac2 + missingfac1 + valuefac3 + valuefac4 + missingfac2
    facnameall = 'facility_name' + facnamebar


    ftypeper = round((totalftype/pfaci*100), 2)
    progressftype = '''<div class="container">
      <div class="progress">
       <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

    valueftype1 = ' aria-valuenow= "{}"'.format(ftypeper)
    valueftype2 = ' style="width:{}%">'.format(ftypeper)
    missingftype1 = str(round(ftypeper, 2)) + '''% Total Facility Type
    
        </div>
    <div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
    valueftype3 = ' aria-valuenow= "{}"'.format(round(perftype, 2))
    valueftype4 = ' style="width:{}%">'.format(round(perftype, 2))
    missingftype2 = str(round(perftype, 2)) + '''% Missing Facility Type
    
        </div>
      </div></b>
    </div>'''

    ftypebar = progressftype + valueftype1 + valueftype2 + missingftype1 + valueftype3 + valueftype4 + missingftype2
    ftypeall = 'facility_type' + ftypebar
else:
    pass

perfirstname = round((totalfirstname/pindi*100), 2)
progressfirstname = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuefirstname1 = ' aria-valuenow= "{}"'.format(perfirstname)
valuefirstname2 = ' style="width:{}%">'.format(perfirstname)
missingfirstname1 = str(round(perfirstname, 2)) + '''% Total First Name

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuefirstname3 = ' aria-valuenow= "{}"'.format(round(perfname, 2))
valuefirstname4 = ' style="width:{}%">'.format(round(perfname, 2))
missingfirstname2 = str(round(perfname, 2)) + '''% Missing Facility Name

    </div>
  </div></b>
</div>'''

firstnamebar = progressfirstname + valuefirstname1 + valuefirstname2 + missingfirstname1 + valuefirstname3 + valuefirstname4 + missingfirstname2
firstall = 'first_name' + firstnamebar

perlastname = round((totallname/pindi*100), 2)
progresslastname = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuelname1 = ' aria-valuenow= "{}"'.format(perlastname)
valuelname2 = ' style="width:{}%">'.format(perlastname)
missinglname1 = str(round(perlastname, 2)) + '''% Total Last Name

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuelname3 = ' aria-valuenow= "{}"'.format(round(perlname, 2))
valuelname4 = ' style="width:{}%">'.format(round(perlname, 2))
missinglname2 = str(round(perlname, 2)) + '''% Missing Last Name

    </div>
  </div></b>
</div>'''

lastnamebar = progresslastname + valuelname1 + valuelname2 + missinglname1 + valuelname3 + valuelname4 + missinglname2
lastall = 'last_name' + lastnamebar

mnameper = round((totalmname/pindi*100), 2)
progressmname = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuemname1 = ' aria-valuenow= "{}"'.format(mnameper)
valuemname2 = ' style="width:{}%">'.format(mnameper)
missingmname1 = str(round(mnameper, 2)) + '''% Total Middle Name

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuemname3 = ' aria-valuenow= "{}"'.format(round(permname, 2))
valuemname4 = ' style="width:{}%">'.format(round(permname, 2))
missingmname2 = str(round(permname, 2)) + '''% Missing Middle Name

    </div>
  </div></b>
</div>'''

mnamebar = progressmname + valuemname1 + valuemname2 + missingmname1 + valuemname3 + valuemname4 + missingmname2
mnameall = 'middle_name' + mnamebar

genper = round((totalgender/pindi*100), 2)
progressgenbar = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuegen1 = ' aria-valuenow= "{}"'.format(genper)
valuegen2 = ' style="width:{}%">'.format(genper)
missinggen1 = str(round(genper, 2)) + '''% Total Gender

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuegen3 = ' aria-valuenow= "{}"'.format(round(pergender, 2))
valuegen4 = ' style="width:{}%">'.format(round(pergender, 2))
missinggen2 = str(round(pergender, 2)) + '''% Missing Gender

    </div>
  </div></b>
</div>'''

genbar = progressgenbar + valuegen1 + valuegen2 + missinggen1 + valuegen3 + valuegen4 + missinggen2
genall = 'gender' + genbar


netper = round((totalnetworks/totalprovider*100), 2)
progressnet = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuenet1 = ' aria-valuenow= "{}"'.format(netper)
valuenet2 = ' style="width:{}%">'.format(netper)
missingnet1 = str(round(netper, 2)) + '''% Total Network

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuenet3 = ' aria-valuenow= "{}"'.format(round(pernet, 2))
valuenet4 = ' style="width:{}%">'.format(round(pernet, 2))
missingnet2 = str(round(pernet, 2)) + '''% Missing Network

    </div>
  </div></b>
</div>'''

netbar = progressnet + valuenet1 + valuenet2 + missingnet1 + valuenet3 + valuenet4 + missingnet2
netall = 'network' + netbar

nettier = round((totaltier/totalprovider*100), 2)
progresstier = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuetier1 = ' aria-valuenow= "{}"'.format(nettier)
valuetier2 = ' style="width:{}%">'.format(nettier)
missingtier1 = str(round(nettier, 2)) + '''% Total Tier

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuetier3 = ' aria-valuenow= "{}"'.format(round(pertier, 2))
valuetier4 = ' style="width:{}%">'.format(round(pertier, 2))
missingtier2 = str(round(pertier, 2)) + '''% Missing Tier

    </div>
  </div></b>
</div>'''

tierbar = progresstier + valuetier1 + valuetier2 + missingtier1 + valuetier3 + valuetier4 + missingtier2
tierall = 'network' + tierbar


grpper = round((totalgrp/totalprovider*100), 2)
progressgrp = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuegrp1 = ' aria-valuenow= "{}"'.format(grpper)
valuegrp2 = ' style="width:{}%">'.format(grpper)
missinggrp1 = str(round(grpper, 2)) + '''% Total Group Aff

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuegrp3 = ' aria-valuenow= "{}"'.format(round(pergrp, 2))
valuegrp4 = ' style="width:{}%">'.format(round(pergrp, 2))
missinggrp2 = str(round(pergrp, 2)) + '''% Missing Group Aff

    </div>
  </div></b>
</div>'''

grpbar = progressgrp + valuegrp1 + valuegrp2 + missinggrp1 + valuegrp3 + valuegrp4 + missinggrp2
grpall = 'group_affiliation' + grpbar

hosper = round((totalhosp/totalprovider*100), 2)
progresshos = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuehos1 = ' aria-valuenow= "{}"'.format(hosper)
valuehos2 = ' style="width:{}%">'.format(hosper)
missinghos1 = str(round(hosper, 2)) + '''% Total Hospital Aff

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuehos3 = ' aria-valuenow= "{}"'.format(round(perhosp, 2))
valuehos4 = ' style="width:{}%">'.format(round(perhosp, 2))
missinghos2 = str(round(perhosp, 2)) + '''% Missing Hospital Aff

    </div>
  </div></b>
</div>'''

hospbar = progresshos + valuehos1 + valuehos2 + missinghos1 + valuehos3 + valuehos4 + missinghos2
hosall = 'hospital_affiliation' + grpbar

specper = round((totalspec/totalprovider*100), 2)
progressspec = '''<div class="container">
  <div class="progress">
   <div class="progress-bar bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valuespec1 = ' aria-valuenow= "{}"'.format(specper)
valuespec2 = ' style="width:{}%">'.format(specper)
missingspec1 = str(round(specper, 2)) + '''% Total Specialties

    </div>
<div class="progress-bar bg-danger" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valuespec3 = ' aria-valuenow= "{}"'.format(round(perspec, 2))
valuespec4 = ' style="width:{}%">'.format(round(perspec, 2))
missingspec2 = str(round(perspec, 2)) + '''% Missing Specialties

    </div>
  </div></b>
</div>'''

specbar = progressspec + valuespec1 + valuespec2 + missingspec1 + valuespec3 + valuespec4 + missingspec2
specall = 'Specialties' + specbar


indiper = round((pindi/(pindi+pfaci)*100), 2)
faciper = round((pfaci/(pindi+pfaci)*100), 2)
progressprov = '''<div class="container">
  <div class="progress">
   <div class="progress-bar progress-bar-striped bg-info" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''

valueprov1 = ' aria-valuenow= "{}"'.format(indiper)
valueprov2 = ' style="width:{}%">'.format(indiper)
prov1 = str(indiper) + '''% Total Individual

    </div>
<div class="progress-bar progress-bar-striped bg-primary" role="progressbar" aria-valuemin="0" aria-valuemax="100"'''
valueprov3 = ' aria-valuenow= "{}"'.format(faciper)
valueprov4 = ' style="width:{}%">'.format(faciper)
prov2 = str(faciper) + '''% Total Facility

    </div>
  </div></b>
</div>'''

barprov = progressprov + valueprov1 + valueprov2 + prov1 + valueprov3 + valueprov4 + prov2

# buttontable = '''<br /><br /><button type="button" class="btn btn-dark" data-toggle="collapse" data-target="#tablebtn">Show Details</button>
#   <div id="tablebtn" class="collapse"><br />'''

table = '''</p></b><div style = "margin-left:6%; margin-right:6%;"><table class="table table-hover">
  <thead>
    <tr>'''
tab1 = '<th scope="col">{}</th>'.format('Fields')
tab2 = '<th scope="col">{}</th>'.format('Available Provider')
tab3 = '<th scope="col">{}</th>'.format('Missing Provider')
tab = '<th scope="col">{}</th>'.format('Bar Distribution')
tab4 = '<th scope="col">{}</th>'.format('Remarks')

table1 = tab1+tab2+tab3+tab+tab4

tables = '''</tr>
  </thead>
  <tbody>
    <tr>'''

tab5 = '<th scope="row">{}</th>'.format('address_string')
tab6 = '<td>{:,}</td>'.format(totaladd)
tab7 = '<td>{:,}</td>'.format(addblank)
tabbaradd = '<td>{}</td>'.format(finaladdbar)
tab8 = '<td>{}</td></tr>\n'.format(result)
table2 = tab5+tab6+tab7+tabbaradd+tab8

tab9 = '<tr><th scope="row">{}</th>'.format('city')
tab10 = '<td>{:,}</td>'.format(totalcity)
tab11 = '<td>{:,}</td>'.format(cityblank)
tabbarcity = '<td>{}</td>'.format(finalcitybar)
tab12 = '<td>{}</td></tr>\n'.format(resultcity)

table3 = tab9+tab10+tab11+tabbarcity+tab12

tablang1 = '<tr><th scope="row">{}</th>'.format('Language')
tablang2 = '<td>{:,}</td>'.format(totallang)
tablang3 = '<td>{:,}</td>'.format(languageblank)
tabbarlang = '<td>{}</td>'.format(langbar)
tablang4 = '<td>{}</td></tr>\n'.format(resutllang)

table4 = tablang1+tablang2+tablang3+tabbarlang+tablang4

tabofc1 = '<tr><th scope="row">{}</th>'.format('Office')
tabofc2 = '<td>{:,}</td>'.format(totaloffice)
tabofc3 = '<td>{:,}</td>'.format(officeblank)
tabbarofc = '<td>{}</td>'.format(ofcbar)
tabofc4 = '<td>{}</td></tr>\n'.format(resultofc)

table5 = tabofc1+tabofc2+tabofc3+tabbarofc+tabofc4

tabphn1 = '<tr><th scope="row">{}</th>'.format('Phone')
tabphn2 = '<td>{:,}</td>'.format(phonetotal)
tabphn3 = '<td>{:,}</td>'.format(phoneblank)
tabbarphn = '<td>{}</td>'.format(phnbar)
tabphn4 = '<td>{}</td></tr>\n'.format(resultphone)

table6 = tabphn1+tabphn2+tabphn3+tabbarphn+tabphn4

state1 = '<tr><th scope="row">{}</th>'.format('State')
state2 = '<td>{:,}</td>'.format(statetotal)
state3 = '<td>{:,}</td>'.format(stateblank)
tabbarstate = '<td>{}</td>'.format(statebar)
state4 = '<td>{}</td></tr>\n'.format(resultstate)

table7 = state1+state2+state3+tabbarstate+state4

zip1 = '<tr><th scope="row">{}</th>'.format('Zip')
zip2 = '<td>{:,}</td>'.format(ziptotal)
zip3 = '<td>{:,}</td>'.format(zipblank)
tabbarzip= '<td>{}</td>'.format(zipall)
zip4 = '<td>{}</td></tr>\n'.format(resultzip)

table8 = zip1+zip2+zip3+tabbarzip+zip4

anp1 = '<tr><th scope="row">{}</th>'.format('accepting_new_patient')
anp2 = '<td>{:,}</td>'.format(anptotal)
anp3 = '<td>{:,}</td>'.format(anpblank)
tabbaranp = '<td>{}</td>'.format(anpbar)
anp4 = '<td>{}</td></tr>\n'.format(resultanp)

table9 = anp1+anp2+anp3+tabbaranp+anp4

npi1 = '<tr><th scope="row">{}</th>'.format('NPI')
npi2 = '<td>{:,}</td>'.format(npitotal)
npi3 = '<td>{:,}</td>'.format(npiblank)
tabbarnpi = '<td>{}</td>'.format(npibar)
npi4 = '<td>{}</td></tr>\n'.format(resultnpi)

table10 = npi1+npi2+npi3+tabbarnpi+npi4

pcp1 = '<tr><th scope="row">{}</th>'.format('PCP')
pcp2 = '<td>{:,}</td>'.format(pcptotal)
pcp3 = '<td>{:,}</td>'.format(pcpblank)
tabbarpcp = '<td>{}</td>'.format(pcpbar)
pcp4 = '<td>{}</td></tr>\n'.format(resultpcp)

table11 = pcp1+pcp2+pcp3+tabbarpcp+pcp4

suid1 = '<tr><th scope="row">{}</th>'.format('site_uid')
suid2 = '<td>{:,}</td>'.format(suidtotal)
suid3 = '<td>{:,}</td>'.format(suidblank)
totalbarsuid = '<td>{}</td>'.format(suidbar)
suid4 = '<td>{}</td></tr>\n'.format(resultsuid)

table12 = suid1+suid2+suid3+totalbarsuid+suid4

uname1 = '<tr><th scope="row">{}</th>'.format('unparsed_name')
uname2 = '<td>{:,}</td>'.format(unametotal)
uname3 = '<td>{:,}</td>'.format(unameblank)
tablebaruname = '<td>{}</td>'.format(unamebar)
uname4 = '<td>{}</td></tr>\n'.format(resultuname)

table13 = uname1+uname2+uname3+tablebaruname+uname4

provcount = '<tr><th scope="row" bgcolor="#DCF4FF">{}</th>'.format('provider_type count')
totalindividual = '<td bgcolor="#DCF4FF"><b><font color="purple">Total Individual: {:,}</td></b></font>'.format(pindi)
totalfacility = '<td bgcolor="#DCF4FF"><b><font color="purple">Total Facility: {:,}</td></b></font>'.format(pfaci)
graphprov = '<td><b><font color="purple">{}</td></b></font>'.format(barprov)

finalprov = provcount + totalindividual + totalfacility + graphprov

if pfaci > 1:
    facname1 = '<tr><th scope="row">{}</th>'.format('facility_name')
    facname2 = '<td>{:,}</td>'.format(totalfname)
    facname3 = '<td>{:,}</td>'.format(fnameblank)
    tablefacbar = '<td>{}</td>'.format(facnamebar)
    facname4 = '<td>{}</td></tr>\n'.format(resultfacname)

    table14 = facname1+facname2+facname3+tablefacbar+facname4

    fatype1 = '<tr><th scope="row">{}</th>'.format('facility_type')
    fatype2 = '<td>{:,}</td>'.format(totalftype)
    fatype3 = '<td>{:,}</td>'.format(ftypeblank)
    tabbarftype = '<td>{}</td>'.format(ftypebar)
    fatype4 = '<td>{}</td></tr>\n'.format(resultftype)

    table15 = fatype1+fatype2+fatype3+tabbarftype+fatype4
else:
    pass

firstname1 = '<tr><th scope="row">{}</th>'.format('first_name')
firstname2 = '<td>{:,}</td>'.format(totalfirstname)
firstname3 = '<td>{:,}</td>'.format(fnameblank)
tabbarfirstname = '<td>{}</td>'.format(firstnamebar)
firstname4 = '<td>{}</td></tr>\n'.format(resultfname)

table16 = firstname1+firstname2+firstname3+tabbarfirstname+firstname4

lname1 = '<tr><th scope="row">{}</th>'.format('last_name')
lname2 = '<td>{:,}</td>'.format(totallname)
lname3 = '<td>{:,}</td>'.format(lnameblank)
tabbarlname = '<td>{}</td>'.format(lastnamebar)
lname4 = '<td>{}</td></tr>\n'.format(resultlname)

table17 = lname1+lname2+lname3+tabbarlname+lname4

mname1 = '<tr><th scope="row">{}</th>'.format('middle_name')
mname2 = '<td>{:,}</td>'.format(totalmname)
mname3 = '<td>{:,}</td>'.format(mnameblank)
tabbarmname = '<td>{}</td>'.format(mnamebar)
mname4 = '<td>{}</td></tr>\n'.format(resultmname)

table18 = mname1+mname2+mname3+tabbarmname+mname4

gen1 = '<tr><th scope="row">{}</th>'.format('gender')
gen2 = '<td>{:,}</td>'.format(totalgender)
gen3 = '<td>{:,}</td>'.format(genderblank)
tabbargen = '<td>{}</td>'.format(genbar)
gen4 = '<td>{}</td></tr>\n'.format(resultgender)

table19 = gen1+gen2+gen3+tabbargen+gen4

net1 = '<tr><th scope="row">{}</th>'.format('network')
net2 = '<td>{:,}</td>'.format(totalnetworks)
net3 = '<td>{:,}</td>'.format(networkblank)
tabbarnet = '<td>{}</td>'.format(netbar)
net4 = '<td>{}</td></tr>\n'.format(resultnet)

table20 = net1+net2+net3+tabbarnet+net4

tier1 = '<tr><th scope="row">{}</th>'.format('tier')
tier2 = '<td>{:,}</td>'.format(totaltier)
tier3 = '<td>{:,}</td>'.format(tierblank)
tabbartier = '<td>{}</td>'.format(tierbar)
tier4 = '<td>{}</td></tr>\n'.format(resulttier)

table21 = tier1+tier2+tier3+tabbartier+tier4

grp1 = '<tr><th scope="row">{}</th>'.format('group_affiliation')
grp2 = '<td>{:,}</td>'.format(totalgrp)
grp3 = '<td>{:,}</td>'.format(grpblank)
tabbargrp = '<td>{}</td>'.format(grpbar)
grp4 = '<td>{}</td></tr>\n'.format(resultgrp)

table22 = grp1+grp2+grp3+tabbargrp+grp4

hos1 = '<tr><th scope="row">{}</th>'.format('hospital_affiliation')
hos2 = '<td>{:,}</td>'.format(totalhosp)
hos3 = '<td>{:,}</td>'.format(hosblank)
tabbarhos = '<td>{}</td>'.format(hospbar)
hos4 = '<td>{}</td></tr>\n'.format(resulthosp)

table23 = hos1+hos2+hos3+tabbarhos+hos4

spec1 = '<tr><th scope="row">{}</th>'.format('Specialties')
spec2 = '<td>{:,}</td>'.format(totalspec)
spec3 = '<td>{:,}</td>'.format(specblank)
tabbarspec = '<td>{}</td>'.format(specbar)
spec4 = '<td>{}</td></tr>\n'.format(resultspec)

table24 = spec1+spec2+spec3+tabbarspec+spec4


tables2 = '''
  </tbody>
</table><hr>'''


provchart = '''<div><div style= "float: left; width:40%; margin-top: -2%; margin-left: 5%;">
<canvas id="myChart2" width="208" height="110"></canvas>
<script>
var ctx = document.getElementById('myChart2').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: '''
datanet = netgrpby
datavalues = ''',datasets: [{
label: ['available count'],
data: '''

datacount = countnet

remp = ''',
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)',
                'rgba(75, 192, 192, 0.8)',
                'rgba(153, 102, 255, 0.8)',
                'rgba(28, 130, 114, 0.8)',
                'rgba(285, 108, 24, 0.8)',
                'rgba(225, 180, 81, 0.8)',
                'rgba(0, 34, 56, 0.8)',
                'rgba(126, 245, 0, 0.8)',
                'rgba(0, 245, 216, 0.8)',
                'rgba(259, 99, 132, 0.8)'
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)',
                'rgba(75, 192, 192, 0.8)',
                'rgba(153, 102, 255, 0.8)',
                'rgba(28, 130, 114, 0.8)',
                'rgba(285, 108, 24, 0.8)',
                'rgba(225, 180, 81, 0.8)',
                'rgba(0, 34, 56, 0.8)',
                'rgba(126, 245, 0, 0.8)',
                'rgba(0, 245, 216, 0.8)',
                'rgba(259, 99, 132, 0.8)'
                
            ],
            borderWidth: 2
        }]
    },
    options: {
        title: {
            display: true,
            fontsize: 14,
            text: 'Network Count'
        },
        legend: {
            display: true,
            position: 'right',
            labels: {
                generateLabels: function(chart) {
                    var data = chart.data;
                    if (data.labels.length && data.datasets.length) {
                        return data.labels.map(function(label, i) {
                            var meta = chart.getDatasetMeta(0);
                            var ds = data.datasets[0];
                            var arc = meta.data[i];
                            var custom = arc && arc.custom || {};
                            var getValueAtIndexOrDefault = Chart.helpers.getValueAtIndexOrDefault;
                            var arcOpts = chart.options.elements.arc;
                            var fill = custom.backgroundColor ? custom.backgroundColor : getValueAtIndexOrDefault(ds.backgroundColor, i, arcOpts.backgroundColor);
                            var stroke = custom.borderColor ? custom.borderColor : getValueAtIndexOrDefault(ds.borderColor, i, arcOpts.borderColor);
                            var bw = custom.borderWidth ? custom.borderWidth : getValueAtIndexOrDefault(ds.borderWidth, i, arcOpts.borderWidth);

							// We get the value of the current label
							var value = chart.config.data.datasets[arc._datasetIndex].data[arc._index];

                            return {
                                // Instead of `text: label,`
                                // We add the value to the string
                                text: label + " : " + value,
                                fillStyle: fill,
                                strokeStyle: stroke,
                                lineWidth: bw,
                                hidden: isNaN(ds.data[i]) || meta.data[i].hidden,
                                index: i
                            };
                        });
                    } else {
                        return [];
                    }
                }
            }
        }
    }
    
});

</script></div></div><br/>'''

allchartp = provchart + str(datanet) + datavalues + str(datacount) + remp
finaldatap = re.sub('data:\s+\[\(', 'data: [', allchartp)
finalchartp = re.sub('\)\]', ']', finaldatap)


statechart = '''<div style="float:right; width:45%; margin-top:-3%; margin-right:5%;">
<canvas id="myChart1" width="235" height="110"></canvas>
<script>
var ctx = document.getElementById('myChart1').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: '''
datastate = stategrby
statevalues = ''',datasets: [{
label: ['available count'],
data: '''

datacount1 = statecount

remp1 = ''',
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)',
                'rgba(75, 192, 192, 0.8)',
                'rgba(153, 102, 255, 0.8)',
                'rgba(28, 130, 114, 0.8)',
                'rgba(285, 108, 24, 0.8)',
                'rgba(225, 180, 81, 0.8)',
                'rgba(0, 34, 56, 0.8)',
                'rgba(126, 245, 0, 0.8)',
                'rgba(0, 245, 216, 0.8)',
                'rgba(259, 99, 132, 0.8)'
               
            ],
            borderColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 206, 86, 0.8)',
                'rgba(75, 192, 192, 0.8)',
                'rgba(153, 102, 255, 0.8)',
                'rgba(28, 130, 114, 0.8)',
                'rgba(285, 108, 24, 0.8)',
                'rgba(225, 180, 81, 0.8)',
                'rgba(0, 34, 56, 0.8)',
                'rgba(126, 245, 0, 0.8)',
                'rgba(0, 245, 216, 0.8)',
                'rgba(259, 99, 132, 0.8)'
                
            ],
            borderWidth: 2
        }]
    },
    options: {
        title: {
            display: true,
            fontsize: 14,
            text: 'State Count'
        },
        legend: {
            display: true,
            position: 'right',
            labels: {
                generateLabels: function(chart) {
                    var data = chart.data;
                    if (data.labels.length && data.datasets.length) {
                        return data.labels.map(function(label, i) {
                            var meta = chart.getDatasetMeta(0);
                            var ds = data.datasets[0];
                            var arc = meta.data[i];
                            var custom = arc && arc.custom || {};
                            var getValueAtIndexOrDefault = Chart.helpers.getValueAtIndexOrDefault;
                            var arcOpts = chart.options.elements.arc;
                            var fill = custom.backgroundColor ? custom.backgroundColor : getValueAtIndexOrDefault(ds.backgroundColor, i, arcOpts.backgroundColor);
                            var stroke = custom.borderColor ? custom.borderColor : getValueAtIndexOrDefault(ds.borderColor, i, arcOpts.borderColor);
                            var bw = custom.borderWidth ? custom.borderWidth : getValueAtIndexOrDefault(ds.borderWidth, i, arcOpts.borderWidth);

							// We get the value of the current label
							var value = chart.config.data.datasets[arc._datasetIndex].data[arc._index];

                            return {
                                // Instead of `text: label,`
                                // We add the value to the string
                                text: label + " : " + value,
                                fillStyle: fill,
                                strokeStyle: stroke,
                                lineWidth: bw,
                                hidden: isNaN(ds.data[i]) || meta.data[i].hidden,
                                index: i
                            };
                        });
                    } else {
                        return [];
                    }
                }
            }
        }
    }    
  

});

</script></div></div></div><br/></div>'''
statechatall = statechart + str(datastate) + statevalues + str(datacount1) + remp1
statefinal = re.sub('data:\s+\[\(', 'data: [', statechatall)
statefinalchart = re.sub('\)\]', ']', statefinal)


if pfaci > 1:
    alltable = finalchartp + statefinalchart + nettableall + statetableall + table + table1 + tables + tables + table2 + table3 + table4 + table5 + table6 + table7 + table8 + table9 + \
           table10 + table11 + table12 + table13 + finalprov + table14 + table15 + table16 +\
           table17 + table18 + table19 + table20 + table21 + table22 + table23 + table24 + tables2
else:
    alltable = finalchartp + statefinalchart + nettableall + statetableall + table + table1 + tables + tables + table2 + table3 + table4 + table5 + table6 + table7 + table8 + table9 + \
               table10 + table11 + table12 + table13 + finalprov + table16 + \
               table17 + table18 + table19 + table20 + table21 + table22 + table23 + table24 + tables2

all = '''
<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

</body>
</html>
'''

with open(filename + '_vericred_summary_report.html', 'w', buffering=90000000) as html:
    html.write(htmlcollapse + reporttitle + totalpro + alltable + all)