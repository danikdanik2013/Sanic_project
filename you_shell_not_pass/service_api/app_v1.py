from sanic.app import Sanic

from .services.authentification.login import LoginForm, LogoutForm
from .services.authentification.registration import RegistationForm


def load_api(app: Sanic):
    app.add_route(RegistationForm.as_view(), '/registration')
    app.add_route(LoginForm.as_view(), '/login')
    app.add_route(LogoutForm.as_view(), '/logout')

