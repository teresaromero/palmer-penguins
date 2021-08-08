from libs.mongo_client import findAll, findByIdAndUpdate

project = {
    "studyname_id": 0,
    "region_id": 0
}


def get_all_individuals(query={}):
    cursor = findAll(
        "individual",
        query,
        project
    )
    return list(cursor)


def find_by_id_and_update(id: str, set: dict):
    return findByIdAndUpdate("individual", id, set, project)
