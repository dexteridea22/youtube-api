"""
Query builder is a generalised pattern for querying
"""
from bson import ObjectId
from flask_mongoengine import Pagination


def get_query_set_filters(query_arguments):
    """
        Universal Query builder for filtering data set
    :param query_arguments: Arguments
    :return: query_set
    """
    raw_query = {}
    for k, v in query_arguments.items():
        if isinstance(v, list):
            if "," in k:
                key = str(k.replace(",id", ""))
                raw_query[key + "__in"] = [ObjectId(x) for x in query_arguments[k]]
            else:
                raw_query[str(k) + "__in"] = query_arguments[k]
        if isinstance(v, tuple):
            raw_query[k + "__gte"] = v[0]
            raw_query[k + "__lte"] = v[1]
    return raw_query


def get_query_set_sort_field(query_arguments):
    """
        Universal Query builder for sorting data set
    :param query_arguments: Arguments
    :return: query_set
    """
    sort_order = (
        ""
        if "sortOrder" in query_arguments and query_arguments["sortOrder"] == "ascend"
        else "-"
    )
    return (
        sort_order + query_arguments["sortField"]
        if "sortField" in query_arguments and query_arguments["sortField"]
        else "created_at"
    )


def pagination(query_set_function, query_arguments, fields):
    """
        paginate query set
    :param fields:
    :param query_set_function: Input query_set function
    :param query_arguments: Filter Arguments
    :return: query set with pagination
    """
    filters = get_query_set_filters(query_arguments)
    sort = get_query_set_sort_field(query_arguments)
    page = query_arguments["page"] if query_arguments["page"] else 1
    page_size = (
        query_arguments["pageSize"]
        if query_arguments["pageSize"] and query_arguments["pageSize"] < 50 + 1
        else 50
    )
    result = Pagination(
        query_set_function(filters=filters, sort=sort, fields=fields),
        page=page,
        per_page=page_size,
    )
    return result
