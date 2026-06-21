def chunked(iterable, n):
    chunk = []

    for item in iterable:
        chunk.append(item)

        if len(chunk) == n:
            yield chunk
            chunk = []

    if chunk:
        yield chunk

print(list(chunked([1, 2, 3, 4, 5, 6, 7], 3)))
print(list(chunked([], 5)))
print(list(chunked(range(10), 4)))