import json
import re
# from tabulate import tabulate
# import pandas as pd

# appenddata = []
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
tier = []
groupaff = []
hospaff = []
spec = []

filename = 'deduped.json'
with open(filename, buffering=90000000) as sumdata:
    size = sum(1 for _ in sumdata)

with open(filename, buffering=90000000) as f:
    for i in f:
        data = json.loads(i)
        dicti = dict(data)
        for lines in data['addresses']:
            addstng = lines['address_string']
            # appenddata.append(a)
            if addstng == '' or None:
                addressblank.append(addstng)

            city = lines['city']
            if city == '' or None:
                cityappend.append(city)

            match = re.search('languages\D+\s\[\]', str(data))
            if match!=None:
                languageappend.append(match)
            # for names in language:
            #     lang = names['name']
            officename = lines['office_name']
            if officename == '' or None:
                officeappend.append(officename)

            phoneval = re.search('phones\D+\s\[\]', str(data))
            if phoneval!=None:
                phoneappend.append(phoneval)

            state = lines['state']
            if state == '' or None:
                stateappend.append(state)

            zip = lines['zip']
            if zip == '' or None:
                zipappend.append(zip)

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
        if site_uid == None or '':
            suid.append(site_uid)

        unpname = dicti['provider']['unparsed_name']
        if unpname == None or '':
            uname.append(unpname)

        protype = dicti['provider']['provider_type']
        if protype == 'facility':
            ptypefac.append(protype)

            facname = dicti['provider']['facility_name']
            if facname == None or '':
                fnameappend.append(facname)

            ftype = dicti['provider']['facility_type']
            if ftype == None or '':
                ftypeappend.append(ftype)

        if protype == 'individual':
            ptypeind.append(protype)

            finame = dicti['provider']['first_name']
            if finame == None or '':
                firstname.append(finame)

            laname = dicti['provider']['last_name']
            if laname == None or '':
                lname.append(laname)

            miname = dicti['provider']['middle_name']
            if miname == None or '':
                mname.append(miname)

            gen = dicti['provider']['gender']
            if gen == None or '':
                gender.append(gen)

        network = re.search('networks\D+\s\[\]', str(data))
        if network!= None:
            networks.append(network)

        for net in data['networks']:
            tiername = net['tier']
            if tiername == None or '':
                tier.append(tiername)

        grpaff = re.search('group_affiliations\"\:\s+\[\]', i)
        if grpaff!= None:
            groupaff.append(groupaff)

        hosaff = re.search('hospital_affiliations\"\:\s+\[\]', i)
        if hosaff != None:
            hospaff.append(hospaff)

        specialities = re.search('specialties\"\:\s+\[\]', i)
        if specialities != None:
            spec.append(specialities)

totalprovider = size
addblank = len(addressblank)
totaladd = totalprovider-addblank
per = (addblank/totalprovider*100)

cityblank = len(cityappend)
totalcity = totalprovider-cityblank
percity = (cityblank/totalprovider*100)

languageblank = len(languageappend)
totallang = totalprovider-languageblank
perlang = (languageblank/totalprovider*100)

officeblank = len(officeappend)
totaloffice = totalprovider-officeblank
peroffice = (officeblank/totalprovider*100)

phoneblank = len(phoneappend)
phonetotal = totalprovider-phoneblank
perphone = (phoneblank/totalprovider*100)

stateblank = len(stateappend)
statetotal = totalprovider-stateblank
perstate = (stateblank/totalprovider*100)

zipblank = len(zipappend)
ziptotal = totalprovider-zipblank
perzip = (zipblank/totalprovider*100)

anpblank = len(accnewpatappend)
anptotal = totalprovider-anpblank
peranp = (anpblank/totalprovider*100)

npiblank = len(npi)
npitotal = totalprovider-npiblank
pernpi = (npiblank/totalprovider*100)

pcpblank = len(pcp)
pcptoral = totalprovider-pcpblank
perpcp = (pcpblank/totalprovider*100)

suidblank = len(suid)
suidtotal = totalprovider-suidblank
persuid = (suidblank/totalprovider*100)

unameblank = len(uname)
unametotal = totalprovider-unameblank
peruname = (unameblank/totalprovider*100)

pindi = len(ptypeind)
perindi = (pindi/totalprovider*100)

pfaci = len(ptypefac)
perfaci = (pfaci/totalprovider*100)

facnameblank = len(fnameappend)
totalfname = pfaci-facnameblank
perfacname = (facnameblank/pfaci*100)

ftypeblank = len(ftypeappend)
totalftype = pfaci-ftypeblank
perftype = (ftypeblank/pfaci*100)

fnameblank = len(firstname)
totalfirstname = pindi-fnameblank
perfname = (fnameblank/pindi*100)

lnameblank = len(lname)
totallname = pindi-lnameblank
perlname = (lnameblank/pindi*100)

mnameblank = len(mname)
totalmname = pindi-mnameblank
permname = (mnameblank/pindi*100)

genderblank = len(gender)
totalgender = pindi-genderblank
pergender = (genderblank/pindi*100)

networkblank = len(networks)
totalnetworks = totalprovider-networkblank
pernet = (networkblank/totalprovider*100)

tierblank = len(tier)
totaltier = totalprovider
pertier = (tierblank/totalprovider*100)

grpblank = len(groupaff)
totalgrp = totalprovider-grpblank
pergrp = (grpblank/totalprovider*100)

hosblank = len(hospaff)
totalhosp = totalprovider-hosblank
perhosp = (hosblank/totalprovider*100)

specblank = len(spec)
totalspec = totalprovider-specblank
perspec = (specblank/totalprovider*100)


if per > 8:
    result = '<hr><b><font color = "red">address_string needs to be fixed!!!</b><hr></font>'
else:
    result = '<hr><b><font color = "green">address_string looks okay!!!</b><hr></font>'

if percity > 8:
    resultcity = '<hr><b><font color = "red">city needs to be fixed!!!</b><hr></font>'
else:
    resultcity = '<hr><b><font color = "green">city looks okay!!!</b><hr></font>'

if perlang > 8:
    resutllang = '<hr><b><font color = "red">language needs to be fixed!!!</b><hr></font>'
else:
    resutllang = '<hr><b><font color = "green">language looks okay!!!</b><hr></font>'

if peroffice > 8:
    resultofc = '<hr><b><font color = "red">office_name needs to be fixed!!!</b><hr></font>'
else:
    resultofc = '<hr><b><font color = "green">office_name looks okay!!!</b><hr></font>'

if perphone > 8:
    resultphone = '<hr><b><font color = "red">phone needs to be fixed!!!</b><hr></font>'
else:
    resultphone = '<hr><b><font color = "green">phone looks okay!!!</b><hr></font>'

if perstate > 8:
    resultstate = '<hr><b><font color = "red">state needs to be fixed!!!</b><hr></font>'
else:
    resultstate = '<hr><b><font color = "green">state looks okay!!!</b><hr></font>'

if perzip > 8:
    resultzip = '<hr><b><font color = "red">zip needs to be fixed!!!</b><hr></font>'
else:
    resultzip = '<hr><b><font color = "green">zip looks okay!!!</b><hr></font>'

if peranp > 8:
    resultanp = '<hr><b><font color = "red">accepting_new_patient needs to be fixed!!!</b><hr></font>'
else:
    resultanp = '<hr><b><font color = "green">accepting_new_patient looks okay!!!</b><hr></font>'

if pernpi > 8:
    resultnpi = '<hr><b><font color = "red">npi needs to be fixed!!!</b><hr></font>'
else:
    resultnpi = '<hr><b><font color = "green">npi looks okay!!!</b><hr></font>'

if perpcp > 8:
    resultpcp = '<hr><b><font color = "red">pcp needs to be fixed!!!</b><hr></font>'
else:
    resultpcp = '<hr><b><font color = "green">pcp looks okay!!!</b><hr></font>'

if persuid > 8:
    resultsuid = '<hr><b><font color = "red">site_uid needs to be fixed!!!</b><hr></font>'
else:
    resultsuid = '<hr><b><font color = "green">site_uid looks okay!!!</b><hr></font>'

if peruname > 8:
    resultuname = '<hr><b><font color = "red">Unparsed Name needs to be fixed!!!</b><hr></font>'
else:
    resultuname = '<hr><b><font color = "green">Unparsed Name looks okay!!!</b><hr></font>'

if perfacname > 8:
    resultfacname = '<hr><b><font color = "red">Facility Name needs to be fixed!!!</b><hr></font>'
else:
    resultfacname = '<hr><b><font color = "green">Facility Name looks okay!!!</b><hr></font>'

if ftypeblank > 8:
    resultftype = '<hr><b><font color = "red">Facility Type needs to be fixed!!!</b><hr></font>'
else:
    resultftype = '<hr><b><font color = "green">Facility Type looks okay!!!</b><hr></font>'

if perfname > 8:
    resultfname = '<hr><b><font color = "red">First Name needs to be fixed!!!</b><hr></font>'
else:
    resultfname = '<hr><b><font color = "green">First Name looks okay!!!</b><hr></font>'

if perlname > 8:
    resultlname = '<hr><b><font color = "red">Last Name needs to be fixed!!!</b><hr></font>'
else:
    resultlname = '<hr><b><font color = "green">Last Name looks okay!!!</b><hr></font>'

if permname > 8:
    resultmname = '<hr><b><font color = "red">Middle Name needs to be fixed!!!</b><hr></font>'
else:
    resultmname = '<hr><b><font color = "green">Middle Name looks okay!!!</b><hr></font>'

if pergender > 8:
    resultgender = '<hr><b><font color = "red">Gender needs to be fixed!!!</b><hr></font>'
else:
    resultgender = '<hr><b><font color = "green">Gender looks okay!!!</b><hr></font>'

if pernet > 8:
    resultnet = '<hr><b><font color = "red">Network needs to be fixed!!!</b><hr></font>'
else:
    resultnet = '<hr><b><font color = "green">Network looks okay!!!</b><hr></font>'

if pertier > 8:
    resulttier = '<hr><b><font color = "red">Network Tier needs to be fixed!!!</b><hr></font>'
else:
    resulttier = '<hr><b><font color = "green">Network Tier looks okay!!!</b><hr></font>'

if pergrp > 8:
    resultgrp = '<hr><b><font color = "red">Group Affiliations need to be fixed!!!</b><hr></font>'
else:
    resultgrp = '<hr><b><font color = "green">Group Affiliations look okay!!!</b><hr></font>'

if perhosp > 8:
    resulthosp = '<hr><b><font color = "red">Hospital Affiliations need to be fixed!!!</b><hr></font>'
else:
    resulthosp = '<hr><b><font color = "green">Hospital Affiliations look okay!!!</b><hr></font>'

if perspec > 8:
    resultspec = '<hr><b><font color = "red">Specialties need to be fixed!!!</b><hr></font>'
else:
    resultspec = '<hr><b><font color = "green">Specialties look okay!!!</b><hr></font>'


htmlcollapse = '''<!DOCTYPE html>
<html>
<head>
<title>Vericred Summary Report</title>
<script src = "https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 48%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
  margin-left: 4%
}

.active, .collapsible:hover {
  background-color: #555;
  margin-left: 4%
  
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
  width: 46%;
  margin-left: 4%
}
</style>
</head>
<body>
<div class = "container">
<h2 style='margin-left:5%;'>Vericred Project Report Summary</h2>
<button class="collapsible">Addresses</button>
<div class="content">
<p><b>'''

totalpro = '<b><font color="purple">Total Provider: {}</font>'.format(totalprovider)
missingadd = '<li>Missing Address String: {} ({}%)</li>'.format(addblank, round(per, 2), '(%)')
totaladdstring = '<li>Total Address String: {}</li>'.format(totaladd)
addressstring = missingadd+totaladdstring+result

citymissing = '<li>Missing City: {} ({}%)</li>'.format(cityblank, round(percity, 2), '(%)')
totalcities = '<li>Total City: {}</li>'.format(totalcity)
cities = citymissing+totalcities+resultcity

langmissing = '<li>Missing Language: {} ({}%)</li>'.format(languageblank, round(perlang, 2), '(%)')
langtotal = '<li>Total Language: {}</li>'.format(totallang)
langu = langmissing+langtotal+resutllang


ofcmissing = '<li>Missing Office: {} ({}%)</li>'.format(officeblank, round(peroffice, 2), '(%)')
ofctotal = '<li>Total Office: {}</li>'.format(totaloffice)
ofc = ofcmissing+ofctotal+resultofc

phonemissing = '<li>Missing Phone: {} ({}%)</li>'.format(phoneblank, round(perphone, 2), '(%)')
phntotal = '<li>Total Phone: {}</li>'.format(phonetotal)
phn = phonemissing+phntotal+resultphone

statemissing = '<li>Missing State: {} ({}%)</li>'.format(stateblank, round(perstate, 2), '(%)')
statetotal = '<li>Total State: {}</li>'.format(statetotal)
stateall = statemissing+statetotal+resultstate

zipmissing = '<li>Missing Zip: {} ({}%)</li>'.format(zipblank, round(perzip, 2), '(%)')
zipstotal = '<li>Total Zip: {}</li></b></p></b>'.format(ziptotal)
zipall = zipmissing+zipstotal+resultzip

addchart = '''<div style="margin-left:3%;">
<canvas id="myChart" width="200" height="100"></canvas>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['address_string', 'city', 'language', 'office', 'phone', 'state','zip'],
        datasets: [{
            label: '# of Votes',
            data: ['''

data1 = addblank
data2 = cityblank
data3 = languageblank
data4 = officeblank
data5 = phoneblank
data6 = stateblank
data7 = zipblank

alldata = data1, data2, data3, data4, data5, data6, data7
rem = '''],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
</script></div>'''
allchart = addchart + str(alldata) + rem
finaldata = re.sub('data:\s+\[\(','data: [', allchart)
finalchart = re.sub('\)\]',']', finaldata)

# allchart = addchart+str(datas)+chart
prov = '''
</div><button class="collapsible">Provider</button>
<div class="content">
<p>
'''


anpmissing = '<b><li>Missing Accepting New Patient: {} ({}%)</li>'.format(anpblank, round(peranp, 2), '(%)')
anpatotal = '<li>Total Accepting New Patient: {}</li>'.format(anptotal)
anpall = totalpro+anpmissing+anpatotal+resultanp

npimissing = '<b><li>Missing NPI: {} ({}%)</li>'.format(npiblank, round(pernpi, 2), '(%)')
npit = '<li>Total NPI: {}</li>'.format(npitotal)
npiall = npimissing+npit+resultnpi

pcpmissing = '<b><li>Missing PCP: {} ({}%)</li>'.format(pcpblank, round(perpcp, 2), '(%)')
pcpt = '<li>Total PCP: {}</li>'.format(pcptoral)
pcpall = pcpmissing+pcpt+resultpcp

suidmissing = '<b><li>Missing Site_Uid: {} ({}%)</li>'.format(suidblank, round(persuid, 2), '(%)')
suidt = '<li>Total Site_Uid: {}</li>'.format(suidtotal)
suidtotal = suidmissing+suidt+resultsuid

unamemissing = '<b><li>Missing Unparsed Name: {} ({}%)</li>'.format(unameblank, round(peruname, 2), '(%)')
unamet = '<li>Total Site_Uid: {}</li>'.format(unametotal)
upnametotal = unamemissing+unamet+resultuname

totalindi = '<font color = "purple"><b>Total Individual Count: {} ({}%)<br>'.format(pindi, round(perindi, 2), '(%)')
totalfac = '<b>Total Facility Count: {} ({}%)</font><hr>'.format(pfaci, round(perfaci, 2), '(%)')
provider = totalindi+totalfac

facnamemissing = '<b><li>Missing Facility Name: {} ({}%)</li>'.format(facnameblank, round(perfacname, 2), '(%)')
facnametotal = '<li>Total Facility Name: {}</li>'.format(totalfname)
factotal = facnamemissing+facnametotal+resultfacname

ftypemissing = '<b><li>Missing Facility Type: {} ({}%)</li>'.format(ftypeblank, round(perftype, 2), '(%)')
ftypetotal = '<li>Total Facility Type: {}</li>'.format(totalftype)
ftypet = ftypemissing+ftypetotal+resultftype

firstnamemissing = '<b><li>Missing First Name: {} ({}%)</li>'.format(fnameblank, round(perfname, 2), '(%)')
firsttotal = '<li>Total First Name: {}</li>'.format(totalfirstname)
firstnametotal = firstnamemissing+firsttotal+resultfname

lnamemissing = '<b><li>Missing Last Name: {} ({}%)</li>'.format(lnameblank, round(perlname, 2), '(%)')
lnametotal = '<li>Total Last Name: {}</li>'.format(totallname)
lastnametotal = lnamemissing+lnametotal+resultlname

mnamemissing = '<b><li>Missing Middle Name: {} ({}%)</li>'.format(mnameblank, round(permname, 2), '(%)')
mnametotal = '<li>Total Middle Name: {}</li>'.format(totalmname)
mitotal = mnamemissing+mnametotal+resultmname

gendermissing = '<b><li>Missing Gender: {} ({}%)</li>'.format(genderblank, round(pergender, 2), '(%)')
gentotal = '<li>Total Gender: {}</li>'.format(totalgender)
gendertotal = gendermissing+gentotal+resultgender


networkhtml = '''
</div><button class="collapsible">Network</button>
<div class="content">
<p>
'''

netmissing = '<b><li>Missing Network: {} ({}%)</li>'.format(networkblank, round(pernet, 2), '(%)')
nettotal = '<li>Total Network: {}</li>'.format(totalnetworks)
networktotal = netmissing+nettotal+resultnet

tiermissing = '<b><li>Missing Tier: {} ({}%)</li>'.format(tierblank, round(pertier, 2), '(%)')
totaltier = '<li>Total Tier: {}</li>'.format(totaltier)
tierall = tiermissing+totaltier+resulttier


affiliation = '''
</div><button class="collapsible">Affiliations</button>
<div class="content">
<p>
'''

groupblank = '<b><li>Missing Group Affiliations: {} ({}%)</li>'.format(grpblank, round(pergrp, 2), '(%)')
totalgroup = '<li>Total Group Affiliations: {}</li>'.format(totalgrp)
grpall = groupblank+totalgroup+resultgrp

hospitalblank = '<b><li>Missing Hospital Affiliations: {} ({}%)</li>'.format(hosblank, round(perhosp, 2), '(%)')
totalhos = '<li>Total Hospital Affiliations: {}</li>'.format(totalhosp)
hospall = hospitalblank+totalhos+resulthosp


speci = '''
</div><button class="collapsible">Specialties</button>
<div class="content">
<p>
'''
specmissing = '<b><li>Missing Specialties: {} ({}%)</li>'.format(specblank, round(perspec, 2), '(%)')
totalspecia = '<li>Total Specialties: {}</li>'.format(totalspec)
specall = specmissing+totalspecia+resultspec


can = '''</p></b>
</div>
<div style="margin-left:50%, margin-top=-20%;"><canvas id="myChart" width="200" height="200"></canvas>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
</script></div></div>
'''

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

</body>
</html>
'''

with open('vericred_summary_report.html', 'w', buffering=90000000) as html:
    html.write(htmlcollapse+totalpro+addressstring+cities+langu+ofc+phn+stateall+zipall+finalchart+
               prov+anpall+npiall+pcpall+suidtotal+upnametotal+provider+factotal+
               ftypet+firstnametotal+lastnametotal+mitotal+gendertotal+networkhtml+
               totalpro+networktotal+tierall+affiliation+totalpro+grpall+hospall+speci+totalpro+specall+all)