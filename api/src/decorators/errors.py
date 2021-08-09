from libs.response import error_response


def handle_error(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            return error_response(str(e))
    wrapper.__name__ = fn.__name__
    return wrapper
