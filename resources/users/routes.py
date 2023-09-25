from flask import request
from uuid import uuid4

from app import app
from db import users, posts

@app.get('/user')
def get_users():
  return {'users': users}, 200

@app.get('/user/<user_id>')
def get_user(user_id):
  try:
    user = users[user_id]
    return user, 200
  except KeyError:
    return {'message': 'user not found'}, 400

@app.post('/user')
def create_user():
  user_data = request.get_json()
  users[uuid4().hex] = user_data
  return user_data, 201

@app.put('/user/<user_id>')
def update_user(user_id):
  user_data = request.get_json()
  try:
    user = users[user_id]
    user['username'] = user_data['username']
    return user, 200
  except KeyError:
    return {'message': 'user not found'}, 400

@app.delete('/user')
def delete_user():
  user_data = request.get_json()
  for i, user in enumerate(users):
    if user['username'] == user_data['username']:
      users.pop(i)
      print(users)
  return {'message':f'{user_data["username"]} deleted'}, 202

@app.get('/user/<user_id>/post')
def get_user_posts(user_id):
  if user_id not in users:
    return {'message': 'user not found'}, 400
  user_posts = [post for post in posts.values() if post['user_id'] == user_id]
  return user_posts, 200