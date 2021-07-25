from flask import Response
import json


def response(data: dict, status: int = 200):
    return Response(
        json.dumps(data),
        status,
        mimetype="application/json",
        content_type="application/json"
    )
