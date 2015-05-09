from core.handler.authorization_handler import AuthorizationHandler
from core.utility.error_exceptions import Error
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(['POST'])
def login(request):
    try:
        request = RequestChecker(request)

        # header

        # POST data
        data = {
            "account": request.get_data("account"),
            "password": request.get_data("password"),
        }
        login_response = AuthorizationHandler.login(data["account"], data["password"])

        # action
        return JSONResponse.output(login_response)

    except Error as error:
        return JSONResponse.output(error)