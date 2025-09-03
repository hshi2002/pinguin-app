from datetime import datetime, timezone
from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import os

def get_db():
    mongo_uri = os.environ.get("MONGO_URI", "mongodb://pinguin:pinguinpass@mongo:27017/pinguin?authSource=admin")
    client = MongoClient(mongo_uri)
    return client.get_default_database()

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "devkey")
    db = get_db()

    @app.get("/api/health")
    def health():
        return {"status": "ok", "time": datetime.now(timezone.utc).isoformat()}

    @app.get("/api/objects")
    def list_objects():
        objs = []
        for doc in db.objects.find().sort("name"):
            doc["_id"] = str(doc["_id"])
            objs.append(doc)
        return jsonify(objs)

    @app.post("/api/objects")
    def add_object():
        data = request.get_json(force=True)
        name = (data.get("name") or "").strip()
        host = (data.get("host") or "").strip()
        interval = int(data.get("interval") or 30)
        if not name or not host or interval < 1:
            return {"error": "name, host and positive interval are required"}, 400
        now = datetime.now(timezone.utc)
        obj = {
            "name": name,
            "host": host,
            "interval": interval,
            "last_status": None,
            "last_checked": None,
            "next_due": now,
        }
        db.objects.insert_one(obj)
        obj["_id"] = str(obj["_id"]) if "_id" in obj else None
        return obj, 201

    @app.delete("/api/objects/<host>")
    def delete_object(host):
        db.objects.delete_one({"host": host})
        return {"deleted": host}

    @app.get("/")
    def index():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)
