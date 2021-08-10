from libs.mongo_client import findAll, findByIdAndUpdate, findAllIndividuals


def get_all(collection: str, query={}, project=None):

    if collection == 'individuals':
        return list(findAllIndividuals())

    cursor = findAll(
        collection,
        query,
        project
    )
    return list(cursor)


def find_by_id_and_update(collection: str, id: str, set: dict, project=None):
    return findByIdAndUpdate(collection, id, set, project)
