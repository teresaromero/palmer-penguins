from libs.query_filter import query_filter
from flask import request
from libs.response import response
from libs.errors import handle_error
from individuals.controllers import get_all_individuals, find_by_id_and_update
from app import app

query_fields = ["studyname:str", "island:str", "region:str", "clutch_completion:bool",
                "sex:str", "culmen_length:float", "body_mass:int", "date_egg:str"]


@app.route("/individuals")
@handle_error
def get_individuals():
    query = query_filter(request.args, query_fields)
    res = get_all_individuals(query)
    return response(res)


@app.route("/individuals/<id>", methods=["PATCH"])
@handle_error
def patch_individual(id):
    body = request.get_json()
    # validate json keys

    res = find_by_id_and_update(id, body)
    return response(res)
