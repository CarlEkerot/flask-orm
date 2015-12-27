from flask import Blueprint, request
import ujson

from webapp import db, cache
from webapp.models.user import User

user = Blueprint('user', __name__)


@user.route('/users', methods=['GET'])
@cache.cached(timeout=1000)
def get_users():
    users = User.query.all()
    return ujson.dumps(User.serialize_list(users))


@user.route('/users/<int:id>', methods=['GET'])
@cache.cached(timeout=1000)
def get_user(id):
    user = User.query.get_or_404(id)
    return ujson.dumps(user.serialize())


@user.route('/users', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']

    user = User(username, password)
    db.session.add(user)
    db.session.commit()

    return ujson.dumps(user.serialize())


@user.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    user.username = request.form['username']
    user.password = request.form['password']
    db.session.commit()

    return ujson.dumps(user.serialize())


@user.route('/users/<int:id>', methods=['DELETE'])
def destroy_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    return "OK"
