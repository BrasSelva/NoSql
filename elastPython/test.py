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


