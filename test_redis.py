import redis
from redis import ConnectionPool
import threading

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('user:1:name', 'John Doe')
r.set('user:1:email', 'john.doe@example.com')

r.setex('session_key', 3600, 'session_data')

user_name = r.get('user:1:name')
user_email = r.get('user:1:email')

user_name = user_name.decode('utf-8')
user_email = user_email.decode('utf-8')

keys = ['user:1:name', 'user:1:email']
values = r.mget(keys)

values = [value.decode('utf-8') for value in values]
print(f"Values: {values}")

pool = ConnectionPool(host='localhost', port=6379, db=0)


def worker():
    r = redis.Redis(connection_pool=pool)
    r.set('nom', 'Alice')
    nom = r.get('nom')
    print(f"Nom récupéré depuis Redis : {nom.decode('utf-8')}")

threads = [threading.Thread(target=worker) for _ in range(5)]

# Démarrer tous les threads
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

