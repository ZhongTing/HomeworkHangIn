from core.account.user_manager import user_manager
from core.homework.homework_manager import homework_manager
from core.utility.error_exceptions import Error
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(["GET"])
def download(request):
    try:
        request = RequestChecker(request)

        # header

        # GET data
        data = {
            "token": request.get_param("token"),
            "homework_id": int(request.get_param("homeworkId")),
        }

        user = user_manager.get_user_from_token(data["token"])
        response = homework_manager.download_homework(data["homework_id"], user)
        return response

    except Error as error:
        return JSONResponse.output(error)