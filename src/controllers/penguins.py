from werkzeug.datastructures import ImmutableMultiDict
from libs.query_filter import query_filter


def getPenguins(request_args: ImmutableMultiDict) -> dict:
    filter_fields = ["studyname:str", "island:str", "region:str", "clutch_completion:bool",
                     "sex:str", "culmen_length:float", "body_mass:int", "date_egg:str"]
    filter = query_filter(request_args, filter_fields)
    limit = request_args.get("limit", default=10, type=int)
    skip = request_args.get("skip", default=0, type=int)
    pass
