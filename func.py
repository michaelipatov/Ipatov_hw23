from typing import Iterable


def filter_query(value, data: Iterable[str]):
    return filter(lambda v: value in v, data)


def map_query(value, data):
    column = int(value)
    return map(lambda v: v.split(' ')[column], data)


def unique_query(data, *args, **kwargs):
    return set(data)


def sort_query(value, data):
    if value == 'asc':
        srt = False
    srt = True
    return sorted(data, reverse=srt)


def limit_query(value, data):
    n = int(value)
    return list(data[:n])
