import redis
import os
from dotenv import load_dotenv

load_dotenv()


client = redis.StrictRedis(host=os.getenv('HOST'), port=6379, decode_responses=True)

for key in client.scan_iter(count=10000):
    if client.type(key) == 'hash':  # Check if the key is a hash
        fields = client.hkeys(key)  # Get only the fields (keys) of the hash
        total_bytes = sum(len(field.encode('utf-8')) for field in fields)
        if total_bytes > 200 :
            print(f"Key: {key} | Size: {total_bytes}B ")