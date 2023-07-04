from pymongo import MongoClient
from read_csvs import csv_to_dictionary_list

def get_connection():
  client = MongoClient("mongodb+srv://user:dIcbhpLhE4wxFhQj@cluster0.ibpst7u.mongodb.net/?retryWrites=true&w=majority")
  return client['pokemones']

def generations_documents():
  generations = csv_to_dictionary_list('csvs/generations.csv')
  db = get_connection()
  db['generations'].insert_many(generations)

def pokemon_types_documents():
  pokemon_types = csv_to_dictionary_list('csvs/pokemon_types.csv')
  db = get_connection()
  db['pokemon_types'].insert_many(pokemon_types)

def locations_documents():
  departments = csv_to_dictionary_list('csvs/departments.csv')
  provinces = csv_to_dictionary_list('csvs/provinces.csv')
  districts = csv_to_dictionary_list('csvs/districts.csv')
  db = get_connection()
  # departemtents
  for doc in departments:
    doc['type'] = 'department'
    doc['parent'] = None # null
  #db['locations'].insert_many(departments)
  # provinces
  for doc in provinces:
    doc['type'] = 'province'
    department_id = db.locations.find_one({'id': doc['department_id'], 'type': 'department'}, {'_id': 1})['_id']
    doc['parent'] = department_id
  #db['locations'].insert_many(provinces)
  # districts
  for doc in districts:
    doc['type'] = 'district'
    province_id = db.locations.find_one({'id': doc['province_id'], 'type': 'province'}, {'_id': 1})['_id']
    doc['parent'] = province_id
  db['locations'].insert_many(districts)
  # delete id field -> javascript code, no python
  # db.locations.updateMany({}, { $unset: { id: "" } })

# pokemon_types_documents()
locations_documents()