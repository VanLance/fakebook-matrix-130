from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  username = fields.Str(required = True)
  email = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True)
  first_name = fields.Str()
  last_name = fields.Str()

class PostSchema(Schema):
  id = fields.Str(dump_only = True)
  body = fields.Str(required = True)
  user_id = fields.Int(required = True)
  timestamp = fields.Str(dump_only=True)
  # user = fields.List(fields.Nested(UserSchema()), dumps_only = True)

class UpdateUserSchema(Schema):
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True, load_only = True)
  new_password = fields.Str()
  first_name = fields.Str()
  last_name = fields.Str()

class DeleteUserSchema(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True)