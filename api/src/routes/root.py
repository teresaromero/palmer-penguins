from libs.validation import validate_route
from flask import request
from libs.response import response
from libs.errors import handle_error
from controllers.root import get_all, find_by_id_and_update
from app import app


@app.route("/<collection>")
@handle_error
@validate_route
def get_collection(collection):
    res = get_all(collection)
    return response(res)


@app.route("/<collection>/<id>", methods=["PATCH"])
@handle_error
@validate_route
def patch_collection_id(collection, id):
    body = request.get_json()
    # validate json keys

    res = find_by_id_and_update(collection, id, body)
    return response(res)
