records = [
    {"id": 3, "priority": 1, "created_at": "2026-01-03"},
    {"id": 1, "priority": 5, "created_at": "2026-01-02"},
    {"id": 2, "priority": 5, "created_at": "2026-01-01"},
    {"id": 4, "created_at": "2026-01-04"},  # no priority
    {"id": 5, "priority": 5, "created_at": "2026-01-01"},
]

def sort_key(record):
    missing_priority = "priority" not in record
    priority = record.get("priority", 0)
    created_at = record.get("created_at")
    id = record["id"]

    return (
        missing_priority,
        -priority,
        created_at,
        id
    )

for record in records:
    print(sort_key(record))

sorted_records = sorted(records, key=sort_key)
print(sorted_records)




