import hug
import marshmallow

class Base(marshmallow.Schema):
    pass

class User(Base):
    name = marshmallow.fields.Str()
    age = marshmallow.fields.Integer()

class UserList(Base):
    collaborators = marshmallow.fields.Nested(User, many=True)

def dumps(f):
    def inner(*args, **kwargs):
        res = f(*args,**kwargs)
        res = UserList(res)
        return res.dumps()
    return inner

@dumps
@hug.post("/")
def index(body: hug.types.MarshmallowSchema(User())):
    print(body)
    user = User(body)
    return [body]


app = __hug_wsgi__
