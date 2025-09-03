import time
from datetime import datetime, timezone, timedelta
from pymongo import MongoClient
import os
from ping_utils import ping_host

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://pinguin:pinguinpass@mongo:27017/pinguin?authSource=admin")
client = MongoClient(MONGO_URI)
db = client.get_default_database()

print("[worker] starting...")

while True:
    now = datetime.now(timezone.utc)
    due = list(db.objects.find({"next_due": {"$lte": now}}))
    for obj in due:
        host = obj.get("host")
        interval = int(obj.get("interval", 30))
        ok = ping_host(host)
        db.objects.update_one(
            {"_id": obj["_id"]},
            {"$set": {
                "last_status": "up" if ok else "down",
                "last_checked": now,
                "next_due": now + timedelta(seconds=interval)
            }}
        )
        print(f"[worker] {host}: {'up' if ok else 'down'}")
    time.sleep(1)
