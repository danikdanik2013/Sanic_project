import pymongo
from sanic import Sanic
from . import app_v1

app = Sanic('myapp')
client = pymongo.MongoClient()
db = client.test_db
collection = db.test_collection

app_v1.load_api(app)
