from flask import request
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from schemas import PostSchema, UpdateUserSchema, UserSchema, DeleteUserSchema
from . import bp
from .models import UserModel

from db import users, posts

@bp.route('/user')
class UserList(MethodView):  
  
  @bp.response(200, UserSchema(many = True))
  def get(self):
    users = UserModel.query.all()
    return users

  @bp.arguments(UserSchema)
  @bp.response(201, UserSchema)
  def post(self, user_data):
    user = UserModel()
    user.from_dict(user_data)
    try:
      user.save()
      return user_data
    except IntegrityError:
      abort(400, message='Username or Email already Taken')

  @bp.arguments(DeleteUserSchema)
  def delete(self, user_data):
    user = UserModel.query.filter_by(username=user_data['username']).first()
    if user and user.check_password(user_data['password']):
      user.delete()
      return {'message':f'{user_data["username"]} deleted'}, 202
    abort(400, message='Username or Password Invalid')

@bp.route('/user/<user_id>')
class User(MethodView):

  @bp.response(200, UserSchema)
  def get(self, user_id):
    user = UserModel.query.get_or_404(user_id, description='User Not Found')
    return user

  @bp.arguments(UpdateUserSchema)
  @bp.response(202, UserSchema)
  def put(self, user_data, user_id):
    user = UserModel.query.get_or_404(user_id, description='User Not Found')
    if user and user.check_password(user_data['password']):
      try:
        user.from_dict(user_data)
        user.save()
        return user
      except IntegrityError:
        abort(400, message='Username or Email already Taken')


@bp.get('/user/<user_id>/post')
@bp.response(200, PostSchema(many=True))
def get_user_posts(user_id):
  if user_id not in users:
    abort(404, message='user not found')
  user_posts = [post for post in posts.values() if post['user_id'] == user_id]
  return user_posts, 200

@bp.route('/user/follow/<follower_id>/<followed_id>')
class FollowUser(MethodView):
  def post(follower_id, followed_id):
    pass

  def put(follower_id, followed_id):
    pass