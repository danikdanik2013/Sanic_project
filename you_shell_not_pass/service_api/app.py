from pymongo import MongoClient
from sanic import Sanic
from . import app_v1

app = Sanic('myapp')

app_v1.load_api(app)
