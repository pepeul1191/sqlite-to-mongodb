import csv

def csv_to_dictionary_list(filename):
  resp = []
  with open(filename, 'r') as file:
    reader = csv.reader(file)
    i = 0
    dict_keys = []
    for row in reader:
      if i == 0:
        dict_keys = row[0].split('|')
        i = i + 1
      else:
        k = 0
        r = row[0].split('|')
        tmp = {}
        while k < len(r):
          tmp[dict_keys[k]] = r[k]
          k = k + 1
        resp.append(tmp)
  return resp

def generations_documents():
  generations = csv_to_dictionary_list('csvs/generations.csv')
  content = '[\n'
  with open('documents/generations.json', 'w') as file:
    for r in generations:
      content = content + '\t{"name": "' + r['name'] + '"},\n'
    file.write(content[:-2] + '\n]')

def pokemon_types_documents():
  pokemon_types = csv_to_dictionary_list('csvs/pokemon_types.csv')
  content = '[\n'
  with open('documents/pokemon_types.json', 'w') as file:
    for r in pokemon_types:
      content = content + '\t{"id": ' +  r['id'] +', "name": "' + r['name'] + '"},\n'
    file.write(content[:-2] + '\n]')

pokemon_types_documents()