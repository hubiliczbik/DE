def top_n(iterable, n):
    counts = {}
    for item in iterable:
        if item not in counts:
            counts[item] = 1
            continue
        else:
            counts[item] += 1
    pairs = list(counts.items())

    sorted_pairs = sorted(
        pairs,
        key=lambda pair: (-pair[1], pair[0]),
    )
    return sorted_pairs[:n]

print(top_n([3, 1, 2], 3))
