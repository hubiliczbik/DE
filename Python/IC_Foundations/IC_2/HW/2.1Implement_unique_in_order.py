items1 = ([1,1,2,2,3,1,1])
items2 = ("AAAABBBCCDAABBB")
items3 = ("xyzzzz")

def unique_in_order(items):
    result = []

    for item in items:
        if not result or item != result[-1]:
            result.append(item)
        else:
            pass
    return result

print(unique_in_order(items1))