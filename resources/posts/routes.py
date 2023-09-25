from flask import request
from uuid import uuid4

from app import app

from db import posts

@app.get('/post')
def get_posts():
  return {'posts': posts}

@app.get('/post/<post_id>')
def get_post(post_id):
  try:
    post = posts[post_id]
    return post, 200
  except KeyError:
    return {'message': 'post not found'}, 400

@app.post('/post')
def create_post():
  post_data = request.get_json()
  posts[uuid4().hex] = post_data
  return post_data, 201

@app.put('/post/<post_id>')
def edit_post(post_id):
  post_data = request.get_json()
  if post_id in posts:
    post = posts[post_id]
    post['body'] = post_data['body']
    return post, 200
  return {'message': 'Post not found'}, 400

@app.delete('/post/<post_id>')
def delete_post(post_id):
  try:
    deleted_post = posts.pop(post_id)
    return {'message':f'{deleted_post["body"]} deleted'}, 202
  except KeyError:
    return {'message': 'Post not found'}, 400
