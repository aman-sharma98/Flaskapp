from flask import Flask
from wtforms import Form
from flask_bcrypt import Bcrypt
from itsdangerous import URLSafeTimedSerializer


app = Flask(__name__)


app.config.from_pyfile('config.cfg')
bcrypt = Bcrypt(app)
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

from questionnaire import routes