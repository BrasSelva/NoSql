import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

document = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

documents = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "bob@example.com", "age": 35}
]
result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)

query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

query = {"age": {"$gt": 25}}
documents = collection.find(query)

for doc in documents:
    print(doc)

query = {"name": "John Doe"}
update = {"$set": {"age": 31}}
result = collection.update_one(query, update)
print("Modified document count:", result.modified_count)

query = {"age": {"$gt": 25}}
update = {"$inc": {"age": 1}}
result = collection.update_many(query, update)
print("Modified document count:", result.modified_count)

query = {"name": "John Doe"}
result = collection.delete_one(query)
print("Deleted document count:", result.deleted_count)

query = {"age": {"$gt": 25}}
result = collection.delete_many(query)
print("Deleted document count:", result.deleted_count)


query = {
    "$and": [
        {"age": {"$gt": 25}},
        {"email": {"$regex": "@example\.com$"}}
    ]
}
documents = collection.find(query)

for doc in documents:
    print(doc)


query = {"age": {"$gt": 25}}
projection = {"_id": 0, "name": 1, "email": 1}
documents = collection.find(query, projection)

for doc in documents:
    print(doc)

query = {"age": {"$gt": 25}}
documents = collection.find(query).sort("name", pymongo.ASCENDING)

for doc in documents:
    print(doc)


import json

with open("accounts.json", "r") as file:
    data = json.load(file)

result = collection.insert_many(data)

print("Inserted data with the following IDs:", result.inserted_ids)


index_name = "city_index"
collection.create_index("address.city", name=index_name)

city = "Bradshawborough"
results = collection.find({"address.city": city})

for result in results:
    print(result)


min_balance = 30000
results = collection.find({"balance": {"$gt": min_balance}})

for result in results:
    print(result)


pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(f"{result['_id']}: {result['total_balance']}")

pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(f"{result['_id']}: {result['total_balance']}")

