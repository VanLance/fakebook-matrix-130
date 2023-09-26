from flask import Flask
from flask_smorest import Api

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

from resources.users import bp as user_bp
api.register_blueprint(user_bp)
from resources.posts import bp as post_bp
api.register_blueprint(post_bp)

from resources.users import routes
from resources.posts import routes
