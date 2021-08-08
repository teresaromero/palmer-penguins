from flask import Response
from pymongo.cursor import Cursor
from bson.json_util import dumps, RELAXED_JSON_OPTIONS


def recoverFilterString(filter: dict) -> str:
    filter_strings = []
    for field in filter:
        print(type(filter[field]))
        if isinstance(filter[field], str):
            filter_strings.append(f"{field}={filter[field]}")
        elif isinstance(filter[field], dict):
            for value in filter[field]:
                filter_strings.append(
                    f"{value[1:]}_{field}={filter[field][value]}")
    return "&" + " & ".join(filter_strings) if filter_strings else ""


def cursor_response(collection: str, documents_cursor: Cursor, total_documents: int, page: int, limit: int, skip: int, filter: dict):
    filter_string = recoverFilterString(filter)
    data = list(documents_cursor)
    return {
        "_page": {
            "current": f"/{collection}?page={page}{filter_string}",
            "prev": f"/{collection}?page={page - 1}{filter_string}" if page > 1 else None,
            "next": f"/{collection}?page={page + 1}{filter_string}" if total_documents - len(data) > 0 else None
        },
        "_metadata": {
            "count_total": total_documents,
            "count_this_page": len(data),
            "filter": filter,
        },
        "data": data,
    }


def response(data, status: int = 200):
    return Response(
        dumps(data, json_options=RELAXED_JSON_OPTIONS),
        status,
        mimetype="application/json",
        content_type="application/json"
    )


def error_response(message, status: int = 500):
    if message == "doc_not_found":
        message = "Document not found"
        status = 404
    if message == "doc_not_updated":
        message = "Document was not updated"
        status = 400
    return response({"error": message, "status_code": status}, status)
