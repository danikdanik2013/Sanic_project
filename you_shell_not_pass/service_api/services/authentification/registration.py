import pymongo
from sanic.response import json
from sanic.views import HTTPMethodView

from service_api.app import session
from service_api.services.messages.message import send_confirmation_email

# MONGO_HOST = "mongodb"
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = "test_db"
client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
collection = db.users_collection


class RegistationForm(HTTPMethodView):

    async def get(self, request):
        return json({"Sorry": "Its get request"})

    async def post(self, request):
        if len(session) == 0:
            return json({'pleas': 'login'})
        data = request.json
        user = data.get('username')
        email = data.get('email')
        check_user = db.users.find({'username': user})
        if check_user.count() == 1:
            return json({'Change username': "please"})
        check_mail = db.users.find({'email': email})
        if check_mail.count() == 1:
            return json({'Change email': "please"})

        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        user_form_to_db = {'username': user, 'password': password,
                           'first_name': first_name, 'last_name':
                               last_name, 'email': email, "confirmed": False}
        users = db.users
        users.insert_one(user_form_to_db)

        send_confirmation_email(email)

        return json({'Method': "post"})

