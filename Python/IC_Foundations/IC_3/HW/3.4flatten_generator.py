def flatten(items):
    for item in items:
        if isinstance(item, (list, tuple)):
            for sub_item in flatten(item):
                yield sub_item
        else:
            yield item


print(list(flatten([1, [2, 3], [4, [5, [6, 7]], 8]])))
print(list(flatten([1, "abc", [2, "def"]])))
print(list(flatten([])))
print(list(flatten([1, [], [2]])))