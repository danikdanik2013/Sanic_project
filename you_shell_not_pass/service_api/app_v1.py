from sanic.app import Sanic

from .services.authentification.registration import RegistationForm


def load_api(app: Sanic):
    print('12312312312312312312312')
    app.add_route(RegistationForm.as_view(), '/registration')


print("asdads")