from enum import unique
from flask import Flask
from model.database import db
from model.user import User
from model.product import Product
import json


# Read Database info
file = open('config.json')
info = json.load(file)
mysql_info = info['mysql']


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@localhost/{}'.format(mysql_info['user'], mysql_info['password'], mysql_info['database'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



@app.route('/')
def index():
    db.create_all()
    return 'ok'

if __name__ == "__main__":
    app.run(debug=True)