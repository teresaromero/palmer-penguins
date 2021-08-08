from libs.mongo_client import validate_collection


def validate_route(fn):
    def wrapper(*args, **kwargs):
        collection = kwargs.get('collection')
        if validate_collection(collection):
            return fn(*args, **kwargs)
        else:
            raise Exception("Collection not valid")
    wrapper.__name__ = fn.__name__
    return wrapper
