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

r_custom = redis.Redis(connection_pool=pool)

def worker():
    r_thread = redis.Redis(connection_pool=pool)
    r_thread.set('user:2:name', 'Jane Doe')
    print(f"Thread Redis Operation: {r_thread.get('user:2:name').decode('utf-8')}")

threads = [threading.Thread(target=worker) for _ in range(5)]

# Démarrer tous les threads
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

r_custom.set('user:3:name', 'Alice Smith')
print(f"User 3 Name: {r_custom.get('user:3:name').decode('utf-8')}")
