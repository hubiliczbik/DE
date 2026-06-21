from select import kevent

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    signature = "".join(sorted(word))

    if signature not in groups:
        groups[signature] = []

    groups[signature].append(word)

result = list(groups.values())

print(result)


def group_anagrams(words):
    groups = {}
    for word in words:
        signature = "".join(sorted(word))

        if signature not in groups:
            groups[signature] = []
        groups[signature].append(word)
    result = list(groups.values())
    return result

print(group_anagrams(words))