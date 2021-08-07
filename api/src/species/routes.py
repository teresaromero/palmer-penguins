from libs.query_filter import query_filter
from flask import request
from libs.response import response
from libs.errors import handle_error
from species.controllers import get_all_species
from app import app

query_fields = ["name:str"]


@app.route("/species")
@handle_error
def get_species():
    query = query_filter(request.args, query_fields)
    res = get_all_species(query)
    return response(res)
