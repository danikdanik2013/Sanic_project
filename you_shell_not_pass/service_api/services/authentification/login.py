from sanic.response import json
from sanic.views import HTTPMethodView
from sanic_auth import User

from service_api.app import app, session
from service_api.app import auth
from .registration import db


@app.middleware('request')
async def add_session(request):
    request['session'] = session


class LoginForm(HTTPMethodView):

    async def get(self, request):
        return json({'change': 'method'})

    async def post(self, request):

        if len(session) != 0:
            return json({'pleas': 'logout'})
        data = request.json
        user = data.get('username')
        password = data.get('password')

        # fetch user from database

        check_user = db.users.find({'username': user})
        password_in_db = db.users.find({'password': password})

        if check_user.count() == 0:
            return json({'User ': "Not found"})
        for x in password_in_db:
            password_mongo = x.get('password')
            username = x.get('username')
            if password_mongo == password and user == username:
                user = User(id=1, name=username)
                auth.login_user(request, user)

                return json({'Your are ': 'login'})

        # message = 'invalid username or password'
        return json({'11': '22'})


class LogoutForm(HTTPMethodView):

    async def post(self, request):
        if len(session) == 0:
            return json({'pleas': 'login'})
        auth.logout_user(request)
        return json({'yesh': '1'})


class UserForm(HTTPMethodView):

    async def get(self, request):
        if len(session) == 0:
            return json({'pleas': 'login'})
        data = request.json
        return json({'test': data})

#
# def handle_no_auth(request):
#     return response.json(dict(message='unauthorized'), status=401)
