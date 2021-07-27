from app import app
from controllers.penguins import getPenguins, getPenguin
from libs.errors import handle_error
from libs.response import response
from flask import request


@handle_error
@app.route("/penguins")
def get_studies():
    result = getPenguins(request.args)
    return response(result)


@handle_error
@app.route("/penguins/<individual_id>")
def get_penguin(individual_id: str):
    result = getPenguin(individual_id, request.args)
    return response(result)
