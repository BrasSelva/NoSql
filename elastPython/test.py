import warnings
from elasticsearch import Elasticsearch
warnings.filterwarnings('ignore')


## Ping du container
import requests
res = requests.get('http://localhost:9200?pretty')
print(res.content)
es = Elasticsearch('http://localhost:9200')


## Create, delete and verify index
#create
print("Create :", es.indices.create(index="first_index",ignore=400))

#verify
print("Verify :", es.indices.exists(index="first_index"))

#delete
print("Delete :", es.indices.delete(index="first_index", ignore=[400,404]))

#create
print("Create :", es.indices.create(index="first_index",ignore=400))

#verify
print("Verify :", es.indices.exists(index="first_index"))

#delete
print("Delete :", es.indices.delete(index="first_index", ignore=[400,404]))

# Insert Document
doc1 = {"city":"New Delhi", "country":"India"}
doc2 = {"city":"London", "country":"England"}
doc3 = {"city":"Los Angeles", "country":"USA"}

#Inserting doc1 in id=1
es.index(index="cities", id=1, body=doc1)

#Inserting doc2 in id=2
es.index(index="cities", id=2, body=doc2)

#Inserting doc3 in id=3
es.index(index="cities", id=3, body=doc3)

# Trouver la fonction qui vérifie que votre index est bien crée.
exists = es.indices.exists(index="cities")
print(f"L'index cities existe: {exists}")

# Récupérer les données avec l'ID :get
retrieve = es.get(index="cities", id=2)
print("Data avec id 2 :", retrieve)

# Afficher uniquement les informations ci-dessous à partir de la variable res
# 'city': 'London', 'country': 'England'}
doc = {"city":"London", "country":"England"}
print("Doc exo :", doc)

## Mapping
print("Mapping :", es.indices.get_mapping(index='cities'))

## Endpoint search
endpoint = es.search(index="cities", body={"query":{"match_all":{}}})
print("Endpoint search : ",endpoint)

# Affiner ces critères de recherche avec _source
source = es.search(index="movies", body={
  "_source": {
    "includes": [
      "*.title",
      "*.directors"
    ],
    "excludes": [
      "*.actors*",
      "*.genres"
    ]
  },
  "query": {
    "match": {
      "fields.directors": "George"
    }
  }
})

print("Search avec _source : ", source)
