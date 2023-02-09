from typing import Optional, Iterable

from func import filter_query, map_query, unique_query, sort_query, limit_query

dict_function = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query
}


def read_file(filename):
    with open(filename) as f:
        for row in f:
            yield row


def query_action(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]):
    if data is None:
        gen = read_file(file_name)
    else:
        gen = data
    res = dict_function[cmd](value=value, data=gen)
    return list(res)
