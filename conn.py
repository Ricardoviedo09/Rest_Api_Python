from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from marshmallow import fields

#Init App
app = Flask(__name__)

#Database
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/pruebapractica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#Init db
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Lunch Schema
class LunchSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    lastname = fields.Str(required=True)
    telephone = fields.Integer()
    email = fields.Str(required=True)
    age = fields.Integer(required=True)
    address = fields.Str()
    food_delivered = fields.Boolean(required=True)
    observation = fields.Str()

#Init Schema
lunch_schema = LunchSchema()
lunchs_schema = LunchSchema(many=True)