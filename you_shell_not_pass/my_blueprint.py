from sanic import Blueprint
from sanic.response import json

bp = Blueprint('my_blueprint')


@bp.route('/')
async def bp_root(request):
    return json({'my': 'blueprint'})
