
from werkzeug.datastructures import ImmutableMultiDict


def parseFilterValue(value, field_type):
    try:
        if field_type == "str":
            return value
        if field_type == "int":
            return int(value)
        if field_type == "float":
            return float(value)
        if field_type == "bool" and value == "true":
            return True
        if field_type == "bool" and value == "false":
            return False
    except ValueError:
        return None


def extractField(request_args: ImmutableMultiDict, field: str, field_type: str):
    try:
        value = request_args.get(f"{field}")
        if value:
            return parseFilterValue(value, field_type)
        return None
    except KeyError:
        return None


def query_filter(request_args: ImmutableMultiDict, filter_fields: list[str]):
    exact_filter = {}
    range_filter = {}
    for field in filter_fields:
        field_name, field_type = field.split(":")
        exact_request_arg = extractField(request_args, field_name, field_type)
        if exact_request_arg != None:
            exact_filter = {**exact_filter, **{field_name: exact_request_arg}}
        if field_type in ["float", "int"]:
            range_types = ["lt", "lte", "gt", "gte"]
            for range_type in range_types:
                range_field_name = f"{range_type}_{field_name}"
                range_request_arg = extractField(
                    request_args, range_field_name, field_type)
                if range_request_arg:
                    range_filter = {
                        **range_filter,
                        **{
                            field_name: {
                                **range_filter[field_name],
                                **{
                                    f"${range_type}": range_request_arg}
                            } if range_filter and range_filter[field_name] else {
                                f"${range_type}": range_request_arg
                            }
                        }
                    }
    return {**exact_filter, **range_filter}
