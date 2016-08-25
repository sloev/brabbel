import hug
from cabaca.core import schema_dumps
from cabaca.schemas import Policy

@hug.post('/policy', output=schema_dumps(Policy))
def policy_post(body):#: hug.types.MarshmallowSchema(Policy)):
    return body
