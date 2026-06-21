import itertools
from collections import Counter


sentences = [
 "the cat sat on the mat",
 "the dog chased the cat",
 "the dog and the cat are friends",
]

pair_counts = Counter()



sentences_split = [sentence.split() for sentence in sentences]
sentences_split_set = [set(sentence.split()) for sentence in sentences]



for words in sentences_split_set:
    for pair in itertools.combinations(words, 2):
        pair = tuple(sorted(pair))
        pair_counts[pair] += 1
print(pair_counts)


