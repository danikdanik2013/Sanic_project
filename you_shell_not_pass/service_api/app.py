from sanic import Sanic
from sanic_auth import Auth

from my_blueprint import bp
from . import app_v1

# from sanic_session import Session

app = Sanic(__name__)
auth = Auth(app)
session = {}
app.config.AUTH_LOGIN_ENDPOINT = 'login'


app_v1.load_api(app)
app.blueprint(bp)


# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
#
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)
