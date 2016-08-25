import hug
from hug.output_format import json
from falcon import HTTP_400

def schema_dumps(schema, doc=None):
    dumps = schema.dumps
    @hug.format.content_type('application/json')
    def schema_handler(content, request, response):
        errors = content.get("errors", {})

        if not errors:
            content, errors = dumps(content)

        if errors:
            response.status = HTTP_400
            return json(errors)

        return content.encode('utf8')

    schema_handler.__doc__ = doc or "json dumped with schema {0}".format(schema)
    return schema_handler
