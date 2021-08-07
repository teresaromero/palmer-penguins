from libs.mongo_client import findAll


def get_all_islands(query={}):
    cursor = findAll(
        "island",
        query)
    return list(cursor)
