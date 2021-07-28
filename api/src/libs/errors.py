from libs.response import response


def error(message, status_code=500):
    return response({
        "status_code": status_code,
        "message": message
    }, status_code)


def handle_error(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            return error(str(e))
    wrapper.__name__ = fn.__name__
    return wrapper
