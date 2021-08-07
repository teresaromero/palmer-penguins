from libs.mongo_client import findAll


def get_all_individuals(query={}):
    cursor = findAll(
        "individual",
        query,
        {
            "studyname_id": 0,
            "region_id": 0
        })
    return list(cursor)
