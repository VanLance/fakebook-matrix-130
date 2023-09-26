from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from schemas import PostSchema
from . import bp
from db import posts

@bp.route('/')
class PostList(MethodView):
  def get(self):
    return {'posts': posts}

  @bp.arguments(PostSchema)
  def post(self, post_data):
    posts[uuid4().hex] = post_data
    return post_data, 201

@bp.route('/<post_id>')
class Post(MethodView):
  
  def get(self, post_id):
    try:
      post = posts[post_id]
      return post, 200
    except KeyError:
      abort(404, message='Post not Found')
      # return {'message': 'post not found'}, 400

  @bp.arguments(PostSchema)
  def put(self, post_data, post_id):
    if post_id in posts:
      post = posts[post_id]
      if post_data['user_id'] != post['user_id']:
        abort(400, message='Cannot edit other users post')
      post['body'] = post_data['body']
      return post, 200
    abort(404, message='Post not Found')

  def delete(self, post_id):
    try:
      deleted_post = posts.pop(post_id)
      return {'message':f'{deleted_post["body"]} deleted'}, 202
    except KeyError:
      abort(404, message='Post not found')
