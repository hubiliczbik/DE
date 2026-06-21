from enum import unique

scores = {"a": 90, "b": 85, "c": 90, "d": 70, "e": 85, "f": 60}
k=2

sortowanie_malejaco = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
#lambda - pozwala powiedziec wedlug czego mam sortowac

unique_scored = sorted(set(scores.values()), reverse=True)
threshold = unique_scored[k - 1]

print(threshold)

