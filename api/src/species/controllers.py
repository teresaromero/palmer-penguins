from libs.mongo_client import findAll


def get_all_species(query={}):
    cursor = findAll(
        "species",
        query)
    return list(cursor)
