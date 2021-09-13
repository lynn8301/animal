from enum import unique
from model.database import db
from datetime import datetime
from sqlalchemy import text

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False, default = '')
    code = db.Column(db.String(255), nullable = False, default = '')
    img = db.Column(db.String(255), unique = True, nullable = False)
    description = db.Column(db.Text, nullable = True)
    state = db.Column(db.String(10), nullable = False)
    update_time = db.Column(db.TIMESTAMP(True), nullable = False)
    created_time = db.Column(db.TIMESTAMP(True), nullable = False, server_default = text('NOW()'))

    def __init__(self, name, price, img, description, state):
        self.name = name
        self.price = price
        self.img = img
        self.description = description
        self.state = state
