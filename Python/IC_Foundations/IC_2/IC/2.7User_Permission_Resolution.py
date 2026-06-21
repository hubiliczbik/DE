def effective_perms(groups, user_groups, denies):
    effective = set()

    for group in user_groups:
        if group not in groups:
            print(f"Warning: group {group} not in user_groups")
            continue

        effective.update(groups[group])
    return effective - denies

groups = {
    "engineers": {"read", "write", "deploy"},
    "interns": {"read"},
    "oncall" : {"read", "alert", "page"},
}
user_groups = ["engineers", "oncall"]
explicit_denies = {"deploy"}

print(effective_perms(groups, user_groups, explicit_denies))




