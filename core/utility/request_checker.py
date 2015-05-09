from core.utility.error_exceptions import ParameterError


class RequestChecker():
    def __init__(self, request):
        self._request = request
        self._error_message = None
        self._checked = {}

    def __str__(self):
        print "- - - - - - - - - -"
        print "Request URL:", self._request.META["PATH_INFO"]
        print "Checked List:", self._checked
        print "Is Valid:", self.is_valid
        params = "PARAMS: " + str(self._request.QUERY_PARAMS)
        data = "DATA: " + str(self._request.DATA)
        return params + "\n" + data

    @property
    def is_valid(self):
        return self._error_message is None

    @property
    def error_message(self):
        return self._error_message

    def get_token(self):
        return self.get_meta("authorization")

    def get_meta(self, key, **arg):
        key = "HTTP_" + key.upper()
        return self._get(self._request.META, key, arg)

    def get_data(self, key, **arg):
        return self._get(self._request.DATA, key, arg)

    def get_param(self, key, **arg):
        return self._get(self._request.QUERY_PARAMS, key, arg)

    def _get(self, request_data, key, arg):
        can_be_null = arg['null'] if 'null' in arg else False
        default_value = arg['default'] if 'default' in arg else None

        if key in request_data:
            value = request_data[key]

        elif can_be_null:
            value = default_value

        else:
            raise ParameterError()

        self._checked[key] = value
        return value