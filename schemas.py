from marshmallow import Schema, fields

class PostSchema(Schema):
  id = fields.Str(dump_only = True)
  body = fields.Str(required = True)
  timestamp = fields.Str(dump_only=True)
  user_id = fields.Int(dump_only = True)

class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  username = fields.Str(required = True)
  email = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True)
  first_name = fields.Str()
  last_name = fields.Str()
  
class UserSchemaNested(UserSchema):
  posts = fields.List(fields.Nested(PostSchema), dump_only=True)
  followed = fields.List(fields.Nested(UserSchema), dump_only=True)

class UpdateUserSchema(Schema):
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True, load_only = True)
  new_password = fields.Str()
  first_name = fields.Str()
  last_name = fields.Str()

class AuthUserSchema(Schema):
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True, load_only = True)