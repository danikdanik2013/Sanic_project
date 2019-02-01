from sanic.response import json
from sanic.views import HTTPMethodView

from service_api.app import auth
from .registration import db


class LoginForm(HTTPMethodView):

    async def get(self, request):
        return json({'change': 'method'})

    async def post(self, request):
        # TODO Add session to login and rebuild login logic
        message = ''
        data = request.json
        user = data.get('username')
        print('*'*100, user, '*'*100)
        password = data.get('password')
        print('*'*100, password, '*'*100)
        # fetch user from database
        user_in_db = db.users.find({'username': user})
        password_in_db = db.users.find({'password': password})
        user_for_check = {}
        for username in user_in_db:
            if username is None:
                return json({"User": "is not avaliable"})
            else:
                print('123')

        print('*'*100, user, '*'*100)
        if user and user.check_password(password):
            auth.login_user(request, user)
            return json({'you': 'login'})
        return json({'Error': '!!!!'})


class LogoutForm(HTTPMethodView):
    @auth.login_required
    async def logout(self, request):
        auth.logout_user(request)
        return json({'You': "logout"})


# @app.route('/profile')
# @auth.login_required(user_keyword='user')
# async def profile(request, user):
#     return response.json({'user': user})
