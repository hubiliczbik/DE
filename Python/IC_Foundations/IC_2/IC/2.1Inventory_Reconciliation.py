from collections import Counter

worker_a = ["bolt", "nut", "nut", "screw", "washer", "bolt", "bolt"]
worker_b = ["bolt", "bolt", "nut", "screw", "screw", "washer"]

worker_a_counter = Counter(worker_a)
worker_b_counter = Counter(worker_b)

all_items = set(worker_a_counter | worker_b_counter)

summary = {}

for item in all_items:
    summary[item] = {
        "a": worker_a_counter[item],
        "b": worker_b_counter[item],
        "diff": worker_a_counter[item] - worker_b_counter[item],
    }
print(summary)