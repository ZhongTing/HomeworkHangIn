from core.account.user_manager import user_manager
from core.homework.homework_manager import homework_manager
from core.utility.error_exceptions import Error, AuthorizationError
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(["POST"])
def upload(request):
    try:
        request = RequestChecker(request)

        # header
        user = user_manager.get_user_from_token(request.get_token())
        if user.is_student:
            raise AuthorizationError()

        # POST data
        data = {
            "homework_id": int(request.get_data("homeworkId")),
            "file": request.get_file("file"),
        }

        homework_manager.upload_homework(data["homework_id"], user, data["file"])

        # action
        return JSONResponse.output()

    except Error as error:
        return JSONResponse.output(error)