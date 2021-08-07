from libs.query_filter import query_filter
from flask import request
from libs.response import response
from libs.errors import handle_error
from islands.controllers import get_all_islands
from app import app

query_fields = ["name:str"]


@app.route("/islands")
@handle_error
def get_islands():
    query = query_filter(request.args, query_fields)
    res = get_all_islands(query)
    return response(res)
