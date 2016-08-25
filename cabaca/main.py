__version__ = 1

import hug

@hug.get('/')
def root(hug_api, hug_api_version):
    return hug_api.http.documentation(api_version=hug_api_version)

@hug.extend_api()
def other_apis():
    from cabaca.api import (
        policy
    )
    return [
        policy
    ]

wsgi_api = __hug_wsgi__
