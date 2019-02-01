from sanic import Sanic
from sanic_auth import Auth
from sanic_session import Session

from . import app_v1

app = Sanic('myapp')
auth = Auth(app)
app.config.AUTH_LOGIN_ENDPOINT = 'login'
Session(app)
app_v1.load_api(app)
