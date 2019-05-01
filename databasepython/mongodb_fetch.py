import pymongo as py
from pymongo import MongoClient

# myclient = pymongo.MongoClient("mongodb://10.5.5.90:27017/")


client = MongoClient()

mydb = client.test_db

datas = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

coll = mydb.data
#
coll.insert_many(datas)
#
# # print(coll.find_one())
#
for x in coll.find():
  print(x)

# coll.drop()

