import itertools


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def group_by_value(iterable):
    grouped = dict()
    for obj in iterable:
        grouped.setdefault(obj.year, []).append(obj)