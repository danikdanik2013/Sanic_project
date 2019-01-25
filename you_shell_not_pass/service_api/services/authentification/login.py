from sanic import response
from sanic.views import HTTPMethodView
from sanic_auth import Auth
from service_api.app import app

from .registration import db

# app = Sanic(__name__)
# app.config.AUTH_LOGIN_ENDPOINT = 'login'
#
#
# @app.middleware('request')
# async def add_session_to_request(request):
#     # setup session
#
auth = Auth(app)


class LoginForm(HTTPMethodView):
    async def login(self, request):
        message = ''
        if request.method == 'POST':
            data = request.json
            user = data.get('username')
            password = data.get('password')
            # fetch user from database
            user = db.users.find({'username': user})
            if user and user.check_password(password):
                auth.login_user(request, user)
                return response.redirect('/profile')
        return response.json({'Its': 'work'})


class LogoutForm(HTTPMethodView):
    @auth.login_required
    async def logout(self, request):
        auth.logout_user(request)
        return response.json({'You': "logout"})


# @app.route('/profile')
# @auth.login_required(user_keyword='user')
# async def profile(request, user):
#     return response.json({'user': user})
