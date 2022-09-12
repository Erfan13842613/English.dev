from uuid import uuid4
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from rq import Queue


def set_config(app):
    app.config['SECRET_KEY'] = str(uuid4())
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    return app


def set_app():
    return Flask(__name__)


def create_app():
    app = set_app()
    return set_config(app)


def create_db(app):
    return SQLAlchemy(app)


def create_redis():
    return redis.Redis()


def create_queue(redis_server):
    return Queue(connection=redis_server)


def create_routes(app):
    from main._Routes_._Base_Route.routes import base
    from main._Routes_._English_Route.routes import english
    
    app.register_blueprint(base)
    app.register_blueprint(english)


app = create_app()
db = create_db(app)
r = create_redis()
q = create_queue(r)
create_routes(app)
