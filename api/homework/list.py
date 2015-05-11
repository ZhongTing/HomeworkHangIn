from core.account.user_manager import user_manager
from core.homework.homework_manager import homework_manager
from core.utility.error_exceptions import Error
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(["GET"])
def list_homework(request):
    try:
        request = RequestChecker(request)

        # header
        user_manager.get_user_from_token(request.get_token())

        # GET data
        data = {
        }

        homework_list = homework_manager.list_homework()

        # action
        return JSONResponse.output({
            "list": homework_list
        })

    except Error as error:
        return JSONResponse.output(error)