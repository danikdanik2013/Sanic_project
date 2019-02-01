import pymongo
from sanic.response import html
from sanic.response import json
from sanic.views import HTTPMethodView

from service_api.app import app, auth
from service_api.services.messages.message import send_mail
from service_api.services.messages.token import generate_confirmation_token, confirm_token

MONGO_HOST = "mongodb"
MONGO_PORT = 27017
MONGO_DB = "test_db"
client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
print(client)
db = client[MONGO_DB]
print(db)
collection = db.users_collection


class RegistationForm(HTTPMethodView):

    # async def add_session(request):
    #    request['session'] = session

    async def get(self, request):
        return json({"Sorry": "Its get request"})

    async def post(self, request):
        data = request.json
        user = data.get('username')
        email = data.get('email')
        check_user = db.users.find({'username': user})
        if check_user.count() == 0:
            return json({'Change email': "please"})
        check_mail = db.users.find({'email': email})
        if check_mail.count() == 0:
            return json({'Change email': "please"})

        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        user_form_to_db = {'username': user, 'password': password,
                           'first_name': first_name, 'last_name':
                               last_name, 'email': email, "confirmed": False}
        print(user_form_to_db)
        users = db.users
        users.insert_one(user_form_to_db)
        token = generate_confirmation_token(email)
        confirm_url = app.url_for(ConfirmingMailForm.confirm_email(token=token, _external=True))
        template = html('/activation.html')
        html_send = template.render('/activation.html', confirm_url=confirm_url)
        send_mail(token, html_send)

        return json({'Method': "post"})


class ConfirmingMailForm(HTTPMethodView):
    @auth.login_required
    def confirm_email(self, token):
        try:
            email = confirm_token(token)
            print(email)
        except:
            print('The confirmation link is invalid or has expired.', 'danger')
        # user = User.query.filter_by(email=email).first_or_404()
        # if user.confirmed:
        #     pass
        #     # flash('Account already confirmed. Please login.', 'success')
        # else:
        #     user.confirmed = True
        #     user.confirmed_on = datetime.datetime.now()
        #     db.session.add(user)
        #     db.session.commit()
        #     # flash('You have confirmed your account. Thanks!', 'success')
        # return redirect(url_for('main.home'))

        return None
