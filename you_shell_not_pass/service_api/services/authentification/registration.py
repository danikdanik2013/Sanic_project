import pymongo
from sanic.response import json
from sanic.views import HTTPMethodView

MONGO_HOST = "mongodb"
MONGO_PORT = 27017
MONGO_DB = "test_db"
client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
print(client)
db = client[MONGO_DB]
print(db)
collection = db.users_collection


class RegistationForm(HTTPMethodView):

    async def get(self, request):
        return json({"Sorry": "Its get request"})

    print('hello')

    async def post(self, request):
        data = request.json
        user = data.get('username')
        email = data.get('email')
        check_user = db.users.find({'username': user})
        for x in check_user:
            print(1)
            if x is not None:
                return json({'Change username': "please"})
        check_mail = db.users.find({'email': email})
        for z in check_mail:
            print(z)
            if z is not None:
                return json({'Change email': "please"})
        if check_user is not None:
            print('12312')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        user_form_to_db = {'username': user, 'password': password,
                           'first_name': first_name, 'last_name': last_name, 'email': email}
        print(user_form_to_db)
        users = db.users
        users.insert_one(user_form_to_db)

        return json({"Method": "POST"})

