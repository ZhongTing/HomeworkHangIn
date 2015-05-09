from core.account.user_manager import UserManager
from core.utility.error_exceptions import Error
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(['POST'])
def login(request):
    try:
        request = RequestChecker(request)

        # header

        # GET data
        data = {
        }

        # action
        return JSONResponse.output()

    except Error as error:
        return JSONResponse.output(error)