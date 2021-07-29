from werkzeug.datastructures import ImmutableMultiDict
from libs.query_filter import query_filter
from libs.mongo import penguins_collection
from bson.json_util import dumps
from libs.response import cursor_response


def getPenguins(request_args: ImmutableMultiDict) -> str:
    filter_fields = ["studyname:str", "island:str", "region:str", "clutch_completion:bool",
                     "sex:str", "culmen_length:float", "body_mass:int", "date_egg:str"]

    filter = query_filter(request_args, filter_fields)

    page_arg = request_args.get("page", default=1, type=int)
    page = page_arg if page_arg >= 0 else 1
    limit = request_args.get("limit", default=10, type=int)
    skip = 0
    
    if page != 0:
        skip = limit*(page-1)
    else:
        limit = 0
    
    total_documents = penguins_collection.count_documents(filter)
    documents_cursor = penguins_collection.find(
        filter, {"_id": 0}).limit(limit).skip(skip)

    result = cursor_response('penguins', documents_cursor,
                             total_documents, page, limit, skip, filter)
    return dumps(result)


def getPenguin(individual_id: str) -> str:
    result = penguins_collection.find_one({"individual_id": individual_id})
    return dumps(result)
