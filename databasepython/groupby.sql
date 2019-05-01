--Networkcount--
select distinct(jsonb_array_elements_text(data->'networks')) as network,count(data->'networks') as countnetwork
from scanhealth where data->'networks'
in (select (data->'networks') from scanhealth) group by data->'networks' having count(*) > 1 order by countnetwork desc;

--providertype--
select distinct(data->'provider'->>'provider_type') as ptype,count(data->'provider'->>'provider_type') as ptypecount
from wellcare where data->'provider'->>'provider_type'
in (select distinct(data->'provider'->>'provider_type') from wellcare) group by data->'provider'->>'provider_type'
having count(*) > 1 order by ptypecount desc;

--specialitycoutn--
select distinct(jsonb_array_elements_text(data->'specialties')) as speciality,count(data->'specialties') as specialitycount
from wellcare where data->'specialties'
in (select data->'specialties' from wellcare) group by data->'specialties' having count(*) > 1 order by specialitycount desc;

select count(distinct(data)) from qualchoicenew;

select distinct(jsonb_array_elements_text(data->'networks')) as network from wellcare order by 1;

select data->'addresses' as address, data->'provider'->>'unparsed_name' as unparsedname,data->'networks' as network,
data->'provider'->>'provider_type' as providertype, data->'provider'->>'facility_type' as facilitytype,data->'provider'->>'first_name'as firstname,
data->'provider'->>'last_name' as lastname,data->'provider'->>'npi' as npi, data->'specialties' as speciality,
data->'group_affiliations' as grpaff, data->'hospital_affiliations' as hospital,data->'provider'->>'gender' as gender,data->'provider'->>'pcp' as pcp
from qualchoicenew order by firstname;

select data->'addresses' as address, data->'provider'->>'unparsed_name' as unparsedname,data->'networks' as network,
data->'provider'->>'provider_type' as providertype, data->'provider'->>'facility_type' as facilitytype,data->'provider'->>'first_name'as firstname,
data->'provider'->>'last_name' as lastname,data->'provider'->>'npi' as npi, data->'specialties' as speciality,
data->'group_affiliations' as grpaff, data->'hospital_affiliations' as hospital,data->'provider'->>'gender' as gender
from pacificsource where data->'provider'->>'provider_type' like '%indi%' order by lastname;

select (data->'provider'->>'unparsed_name') as unparsedname, data->'provider'->>'gender' as gender from qualchoice;








