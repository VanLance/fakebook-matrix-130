from flask_smorest import Blueprint

bp = Blueprint('posts', __name__, url_prefix='/post')

from . import routes