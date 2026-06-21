old = [
    {"id": 1, "name": "Anna", "age": 28},
    {"id": 2, "name": "Piotr", "age": 35},
]
new = [
    {"id": "1", "name": "Anna", "country": "PL"},
    {"id": "2", "name": "Piotr", "country": "PL"},
]

def dif_schema(records):
    schema = {}
    for record in records:
        for column, value in record.items():
            if column not in schema and value is not None:
                schema[column] = type(value)
    return schema

old_schema = dif_schema(old)
new_schema = dif_schema(new)

print(old_schema)
print(new_schema)

old_columns = set(old_schema.keys())
new_columns = set(new_schema.keys())

added = new_columns - old_columns
removed = old_columns - new_columns

print("added:", added)
print("removed:", removed)
print("old_schema:", old_schema)
print("new_schema:", new_schema)

type_changed = {}
common_columns = old_columns & new_columns

for column in common_columns:
    if old_schema[column] != new_schema[column]:
        type_changed[column] = old_schema[column], new_schema[column]

print("type_changed:", type_changed)
