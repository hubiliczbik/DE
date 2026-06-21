files = [
    {"name": "a.txt", "content": "hello"},
    {"name": "b.txt", "content": "world"},
    {"name": "c.txt", "content": "hello"},
]

def find_duplicates(files):
    grouped = {}

    for file in files:
        name = file["name"]
        content = file["content"]

        if content not in grouped:
            grouped[content] = []
        grouped[content].append(name)
    duplicates = {}
    for content, names in grouped.items():
        if len(names) >= 2:
            duplicates[content] = names
    return duplicates

print(find_duplicates(files))