from core.utility.error_exceptions import Error
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class JSONResponse():
    def __init__(self):
        pass

    @staticmethod
    def output(result="", response_code=200):
        if type(result) is list:
            raise Exception("[JSONResponse] Result cannot be list!")

        if isinstance(result, Error):
            content = result.message
            response_code = result.status_code

        else:
            content = JSONRenderer().render(result) if type(result) is dict else result

        return HttpResponse(content, status=response_code, content_type="application/json")
