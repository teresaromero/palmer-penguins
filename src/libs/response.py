from flask import Response
from pymongo.cursor import Cursor


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
    return {
        "_page": {
            "current": f"/{collection}?page={page}{filter_string}",
            "prev": f"/{collection}?page={page - 1}{filter_string}" if page > 1 else None,
            "next": f"/{collection}?page={page + 1}{filter_string}" if total_documents - skip > 0 else None
        },
        "_metadata": {
            "count_total": total_documents,
            "count_this_page": limit,
            "filter": filter,
        },
        "data": list(documents_cursor),
    }


def response(data: str, status: int = 200):
    return Response(
        data,
        status,
        mimetype="application/json",
        content_type="application/json"
    )
