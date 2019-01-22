import pymongo
from sanic.response import json
from sanic.views import HTTPMethodView


client = pymongo.MongoClient()
db = client.test_db
collection = db.users_collection

def foo():
    print("bar")


class RegistationForm(HTTPMethodView):

    async def get(self, request):
        return json({"Sorry": "Its get request"}), 400

    print('hello')

    async def post(self, request):
        data = request.json
        user = data.get('username')
        email = data.get('email')

        # def check_indentification(user, email):
        #     #flag = False
        #     check_user = db.find({'user': user})
        #     check_email = db.find({'email': email})
        #     if check_email is None and check_user is None:
        #         return True
        #     return flag

        #check = check_indentification(user, email)

        # if check is True:
        check_user = db.get.collection.find({'username': user})
        print(check_user)
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
    #else:
     #   return json({'Sorry': "Enter another pass or email"}), 401
