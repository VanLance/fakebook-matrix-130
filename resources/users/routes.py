from flask import request
from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort

from schemas import UpdateUserSchema, UserSchema
from . import bp
from db import users, posts

@bp.route('/user')
class UserList(MethodView):  
  
  def get(self):
    return {'users':list(users.values())}, 200
  
  @bp.arguments(UserSchema)
  def post(self, user_data):
    users[uuid4().hex] = user_data
    return user_data, 201

  def delete(self ):
    user_data = request.get_json()
    for i, user in enumerate(users):
      if user['username'] == user_data['username']:
        users.pop(i)
        print(users)
    return {'message':f'{user_data["username"]} deleted'}, 202

@bp.route('/user/<user_id>')
class User(MethodView):
  def get(self, user_id):
    try:
      user = users[user_id]
      return user, 200
    except KeyError:
      abort(404, message='user not found')

  @bp.arguments(UpdateUserSchema)
  def put(self, user_data, user_id):
    try:
      user = users[user_id]
      if user['password'] != user_data['password']:
        abort(400, message='Incorrect Password')
      # user.update(user_data)
      user |= user_data
      if 'new_password' in user_data:
        new_password = user.pop('new_password')
        user['password'] = new_password
      return user, 200
    except KeyError:
      abort(404, message='user not found')


@bp.get('/user/<user_id>/post')
def get_user_posts(user_id):
  if user_id not in users:
    abort(404, message='user not found')
  user_posts = [post for post in posts.values() if post['user_id'] == user_id]
  return user_posts, 200