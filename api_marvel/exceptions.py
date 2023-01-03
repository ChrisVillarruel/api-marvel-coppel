from requests import Response


class APIMarvelException(Exception):
    def __init__(self, status: str, code: str):
        self.status = status
        self.code = code


class ErrorAPIMarvel(APIMarvelException):
    """ Cualquier error de la api que se regrese  """


class UnknownError(APIMarvelException):
    """ Cualquier error de la api que se regrese  """


def _raise_error_response(data: dict) -> bool:
    error_code = data.get("code")
    messsage = data.get("status")

    if error_code == 200:
        return True
    elif error_code >= 400:
        raise ErrorAPIMarvel(status=messsage, code=error_code)
    else:
        raise UnknownError(status="Error desconocido", code="101")


def _check_response(response: Response):
    _raise_error_response(response.json())
