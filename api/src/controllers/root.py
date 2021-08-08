from libs.mongo_client import findAll, findByIdAndUpdate


def get_all(collection: str, query={}, project=None):
    cursor = findAll(
        collection,
        query,
        project
    )
    return list(cursor)


def find_by_id_and_update(collection: str, id: str, set: dict, project=None):
    return findByIdAndUpdate(collection, id, set, project)
