from core.account.user_manager import user_manager
from core.homework.homework_manager import homework_manager
from core.utility.error_exceptions import Error, AuthorizationError
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(["POST"])
def create(request):
    print "hello"
    try:
        request = RequestChecker(request)

        # header
        user = user_manager.get_user_from_token(request.get_token())
        if not user.is_ta:
            raise AuthorizationError()

        # POST data
        data = {
            "year": request.get_data("year"),
            "name": request.get_data("name"),
            "total_score": request.get_data("totalScore"),
        }
        homework_manager.create_homework(data)

        # action
        return JSONResponse.output()

    except Error as error:
        return JSONResponse.output(error)