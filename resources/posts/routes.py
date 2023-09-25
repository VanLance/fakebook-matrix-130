from app import app

@app.get('/post')
def get_posts():
  pass

@app.post('/post')
def create_post():
  pass

@app.put('/post')
def edit_post():
  pass

@app.delete('/post')
def delete_post():
  pass