from core.utility.error_exceptions import Error
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker
from rest_framework.decorators import api_view


@api_view(["POST"])
def upload(request):
    try:
        request = RequestChecker(request)

        # header

        # POST data
        data = {
            "year": request.get_data("account"),
            "homework_name": request.get_data("name"),
            "total_score": request.get_data("totalScore"),
        }

        # action
        return JSONResponse.output()

    except Error as error:
        return JSONResponse.output(error)