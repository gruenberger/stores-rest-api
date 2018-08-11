import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db') #connects to Heroku's env variables first OR local sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to know when changes were made AND NOT made to db.  turning it off here
app.secret_key = 'andrew'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList,'/stores')

if __name__ == '__main__':
    from db import db
    db.init_app(app) #importing here because of circular imports
    app.run(port=5000, debug=True)
